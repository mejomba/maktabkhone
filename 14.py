from bs4 import BeautifulSoup
import re
import requests
import mysql.connector

'''set connection'''
cnx = mysql.connector.connect(user='mejomba',
                              password='09360521688',
                              host='127.0.0.1',
                              database='maktabkhone'
                              )
cursor = cnx.cursor()
print('connected to ', cnx.database, 'with user', cnx.user)

'''initial parameter'''
table_name = 'car'
fields = ['cost', 'work']

'''create table if not exist'''
try:
    cursor.execute(f'CREATE TABLE {table_name} ({fields[0]} char(50), {fields[1]} char(50));')
    print(f'table {table_name} created.')
except:
    print(f'some thing wrong OR table {table_name} already exists.')


bama_url = 'https://google.com/url?q=https://bama.ir'
next_page = '?page='

pattern = r'href=\"/url(.*)\"><'
pattern2 = r'^/url\?q=https://bama.ir(.*)'
search = input()
bama = 'باما'
if bama not in search:
    search = search + ' باما'
print(search)
counter = 0
page_number = 0
while counter < 20:
    page_number += 1
    g_search = requests.get('https://www.google.com/search?q='+search)
    print('g_search', g_search.status_code)
    soup = BeautifulSoup(g_search.text, 'html.parser')
    all_link = soup.find_all('a', href=True)

    for link in all_link:
        if counter == 20:
            print("20 RECORD Complete.")
            break
        zero = 'کارکرد صفر'
        des = 'در توضیحات'
        agree = 'توافقی'
        draft = 'حواله'
        pre = 'پیش'
        toman  = 'تومان'
        link_bama = re.findall(pattern2, link['href'])
        if link_bama:
            link_to_bama = bama_url+link_bama[0]
            #print(bama_url+link_bama[0])
            bama_page = requests.get(link_to_bama)
            #print(type(bama_page.url))
            #print(link_to_bama)
            #print('bama_page', bama_page.status_code)
            print(bama_page.url)
            bama_page = requests.get(bama_page.url + '/?page=' + str(page_number))
            print(bama_page.url)
            soup = BeautifulSoup(bama_page.text, 'html.parser')
            p_cost = soup.find_all('p', {'class': 'cost'})# contain cost of car
            p_work = soup.find_all('p', {'class': 'price hidden-xs'})# contain work of car

            for cost, work in zip(p_cost, p_work):

                if counter == 20:
                    print("20 RECORD Complete.")
                    break
                elif des in cost.text.strip() or agree in cost.text.strip() or draft in cost.text.strip() or work.text.strip() == '-':
                    print('بدونه قیمت یا کارکرد مشخص')
                else:
                    worke = ''
                    T = re.search(r'(.+\d)', cost.text).group(1)
                    toman = ''
                    toman = toman.join(T)
                    if work.text.strip() == zero:
                        work = '0'
                        print(f'cost=  {toman}, work=  {work}')
                        query = f"INSERT INTO {table_name} ({fields[0]}, {fields[1]}) values ('{toman}', '{work}');"
                        try:
                            cursor.execute(query)
                            cnx.commit()
                            counter += 1
                            print(f"INSERT {counter}th RECORD...")
                        except:
                            print('fail to insert database')
                    else:
                        work = re.findall(r'([0-9])', work.text)
                        worke = worke.join(work)
                        print(f'cost=  {toman}, work=  {worke}')
                        query = f"INSERT INTO {table_name} ({fields[0]}, {fields[1]}) values ('{toman}', '{worke}');"
                        try:
                            cursor.execute(query)
                            cnx.commit()
                            counter += 1
                            print(f"INSERT {counter}th RECORD...")
                        except:
                            print('fail to insert database')
            break

cursor.close()
cnx.close()
