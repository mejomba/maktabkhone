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
print('connected to ', cnx)

'''initial parameter'''
table_name = 'user_info'
fields = ['username', 'password']

'''create table if not exist'''
try:
    cursor.execute(f'CREATE TABLE {table_name} ({fields[0]} char(50), {fields[1]} char(50));')
    print(f'table {table_name} created.')
except:
    print(f'some thing wrong OR table {table_name} already exists.')

bama_url = 'https://google.com/url?q=https://bama.ir'

pattern = r'href=\"/url(.*)\"><'
pattern2 = r'^/url\?q=https://bama.ir(.*)'
search = input()
#g_search = requests.get('https://www.google.com/search?q=%D9%BE%D8%B1%D8%A7%DB%8C%D8%AF+%D8%A8%D8%A7%D9%85%D8%A7')
g_search = requests.get('https://www.google.com/search?q='+search)
print('g_search', g_search.status_code)
soup = BeautifulSoup(g_search.text, 'html.parser')
all_link = soup.find_all('a', href=True)
'''
for a in soup.find_all('a', href=True):
    print ("Found the URL:", a['href'])
'''
for link in all_link:
    link_bama = re.findall(pattern2, link['href'])
    if link_bama:
        link_to_bama = bama_url+link_bama[0]
        print(bama_url+link_bama[0])
        bama_page = requests.get(link_to_bama)
        print('bama_page', bama_page.status_code)
        soup = BeautifulSoup(bama_page.text, 'html.parser')
        div_price = soup.find_all('p', {'class': 'cost'})
        div_working = soup.find_all('p', {'class': 'price hidden-xs'})
        zero = 'کارکرد صفر'
        pricesx = []
        workingx = []
        for str_pricex, str_workingx in zip(div_price, div_working):
            if str(str_pricex.text) == zero:
                digit_pricex = '0'
            else:
                digit_pricex = re.findall(r'[0-9]', str(str_pricex.text))
                digit_pricex = ''.join(digit_pricex)
            if digit_pricex and digit_workingx:
                pricesx.append(digit_pricex)

            digit_workingx = re.findall(r'[0-9]', str(str_workingx))
            digit_workingx = ''.join(digit_workingx)
            if digit_pricex and digit_workingx:
                workingx.append(digit_workingx)
            print('digitprice= ', digit_pricex)
            print('digit working= ', digit_workingx)
        print('pricesx', pricesx)
        print('workingx', workingx)
        for price, work in zip(pricesx, workingx):
            print(price, work)
        break

        '''prices = []
        for str_price in div_price:
            if str(str_price.text) == zero:
                digit_price = '0'
            else:
                digit_price = re.findall(r'[0-9]', str(str_price.text))
                digit_price = ''.join(digit_price)
            print(digit_price)
            
            if digit_price:
                prices.append(digit_price)

        working = []
        for str_work in div_working:
            digit_working = re.findall(r'[0-9]', str(str_work))
            digit_working = ''.join(digit_working)
            if digit_working:
                working.append(digit_working)

        for price, work in zip(prices, working):
            print('price= ', price, 'work= ',work)
        break'''

    #link_text = re.sub(r'\s+', ' ', link.text)
    #print(link_text)
