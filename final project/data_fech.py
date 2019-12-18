from bs4 import BeautifulSoup
import re
import requests
import mysql.connector
from jalaali import Jalaali
from datetime import date,datetime
start = datetime.now()


today = str(date.today()).split('-')
today_jalali = Jalaali.to_jalaali(int(today[0]), int(today[1]), int(today[2]))
#x = today_jalali['jy']
tehran = 420
isfahan = 70
alborz = 40
mazandaran = 22
az_sh = 17
kerman = 10
five = 5
zero = 'کارکرد صفر'
des = 'در توضیحات'
agree = 'توافقی'
draft = 'حواله'
pre = 'پیش'
pre_sel = 'پیش فروش'
toman  = 'تومان'
kartx ='کارتکس'
bama_urls = [
    'https://bama.ir/car/all-brands/all-models/all-trims?province=tehran&hasprice=true',
    'https://bama.ir/car/all-brands/all-models/all-trims?province=isfahan&hasprice=true',
    'https://bama.ir/car/all-brands/all-models/all-trims?province=alborz&hasprice=true',
    'https://bama.ir/car/all-brands/all-models/all-trims?province=mazandaran&hasprice=true',
    'https://bama.ir/car/all-brands/all-models/all-trims?province=razavi-khorasan&hasprice=true',
    'https://bama.ir/car/all-brands/all-models/all-trims?province=azarbaijan-sharghi&hasprice=true',
    'https://bama.ir/car/all-brands/all-models/all-trims?province=fars&hasprice=true',
    'https://bama.ir/car/all-brands/all-models/all-trims?province=kerman&hasprice=true',
    'https://bama.ir/car/all-brands/all-models/all-trims?province=azarbaijan-gharbi&hasprice=true',
    'https://bama.ir/car/all-brands/all-models/all-trims?province=qazvin&hasprice=true',
    'https://bama.ir/car/all-brands/all-models/all-trims?province=kermanshah&hasprice=true',
    'https://bama.ir/car/all-brands/all-models/all-trims?province=golestan&hasprice=true',
    'https://bama.ir/car/all-brands/all-models/all-trims?province=hamedan&hasprice=true',
    'https://bama.ir/car/all-brands/all-models/all-trims?province=gilan&hasprice=true',
    'https://bama.ir/car/all-brands/all-models/all-trims?province=markazi&hasprice=true',
    'https://bama.ir/car/all-brands/all-models/all-trims?province=yazd&hasprice=true',
    'https://bama.ir/car/all-brands/all-models/all-trims?province=yazd&hasprice=true',
    'https://bama.ir/car/all-brands/all-models/all-trims?province=semnan&hasprice=true',
    'https://bama.ir/car/all-brands/all-models/all-trims?province=qom&hasprice=true',
    'https://bama.ir/car/all-brands/all-models/all-trims?province=kordestan&hasprice=true',
    'https://bama.ir/car/all-brands/all-models/all-trims?province=ardebil&hasprice=true',
    'https://bama.ir/car/all-brands/all-models/all-trims?province=zanjan&hasprice=true',
    'https://bama.ir/car/all-brands/all-models/all-trims?province=khuzestan&hasprice=true',
    'https://bama.ir/car/all-brands/all-models/all-trims?province=chaharmahal-bakhtiari&hasprice=true',
    'https://bama.ir/car/all-brands/all-models/all-trims?province=hormozgan&hasprice=true',
    'https://bama.ir/car/all-brands/all-models/all-trims?province=north-khorasan&hasprice=true',
    'https://bama.ir/car/all-brands/all-models/all-trims?province=lorestan&hasprice=true',
    'https://bama.ir/car/all-brands/all-models/all-trims?province=bushehr&hasprice=true',
    'https://bama.ir/car/all-brands/all-models/all-trims?province=sistan-baluchestan&hasprice=true',
    'https://bama.ir/car/all-brands/all-models/all-trims?province=south-khorasan&hasprice=true',
    'https://bama.ir/car/all-brands/all-models/all-trims?province=ilam&hasprice=true',
    'https://bama.ir/car/all-brands/all-models/all-trims?province=kohkiluyeh-boyerahmad&hasprice=true'
]


'''set connection'''
cnx = mysql.connector.connect(user='mejomba',
                              password='09360521688',
                              host='127.0.0.1',
                              database='maktabkhone'
                              )
cursor = cnx.cursor()

'''initial parameter'''
table_name = 'cars'
fields = ['name', 'work', 'price', 'pd', 'city', 'id', 'age']

try:
    cursor.execute(
        f'CREATE TABLE {table_name} ({fields[5]} int primary key auto_increment, {fields[0]} char(80), {fields[1]} int, {fields[2]} bigint,'
        f' {fields[3]} int, {fields[4]} char(25), {fields[6]} int);')
    print(f'table {table_name} created.')
except:
    print(f'some thing wrong OR table {table_name} already exists.')

class Data_fetch(object):
    def __init__(self):
        pass

    def search(self, search_input):
        """get search query from user & search in google for find target URL"""
        pass

    def fetch_data(self):
        """get URL from 'search' & fetch data while 150 record fetched
        send ARRAY to DB_manager for insert into database"""
        self.record_counter = 0
        self.c = 0
        for first_bama_url in bama_urls:
            self.c += 1
            if self.c == 1:
                for i in range(1, tehran):
                    bama_url = f'{first_bama_url}&page={i}'
                    print(bama_url)
                    page_request = requests.get(bama_url)
                    soup = BeautifulSoup(page_request.text, 'html.parser')
                    p_cost = soup.find_all('p', {'class': 'cost'})  # contain cost of car
                    p_work = soup.find_all('p', {'class': 'price hidden-xs'})  # contain work of car
                    h2_name = soup.find_all('h2', {'class': 'persianOrder'})
                    span_pd = soup.find_all('span', {'class': 'price year-label hidden-xs'})
                    #p_city = soup.find_all('span', {'class': 'provice-mobile'})
                    p_city = re.findall(r'province=(.+)&', first_bama_url)[0]

                    for cost, work, name, year in zip(p_cost, p_work, h2_name, span_pd):
                        if des in cost.text.strip() or pre_sel in cost.text.strip() or agree in cost.text.strip() or draft in cost.text.strip() or work.text.strip() == '-' or work.text.strip() == kartx:
                            print('بدونه قیمت یا کارکرد مشخص')
                            pass

                        else:
                            worke = ''
                            T = re.search(r'(.+\d)', cost.text).group(1)
                            toman = ''
                            for n in T:
                                if n.isdigit():
                                    toman += n
                            toman = int(toman)
                            if work.text.strip() == zero:
                                work = '0'
                                work = int(work)
                                c_name = re.findall(r"(.*)\s", name.text, re.MULTILINE)
                                car_name = ''
                                for z in c_name:
                                    car_name += str(z).strip()
                                x = year.text.strip()
                                pd = ''
                                for w in x:
                                    if str(w).isdigit():
                                        pd += w
                                # calculate age of car
                                if int(pd) > 1900:
                                    age = int(today[0]) - int(pd)
                                elif int(pd) <= 1900:
                                    age = today_jalali['jy'] - int(pd)
                                self.record_counter += 1
                                '''set SQL Query'''
                                query = f'INSERT INTO {table_name} ({fields[0]}, {fields[1]}, {fields[2]},{fields[3]}, {fields[4]}, {fields[6]}) VALUES("{car_name}", {work}, {toman}, {pd}, "{p_city}", {age});'
                                cursor.execute(query)
                                cnx.commit()
                                print(f'insert into DB{self.record_counter}')
                            else:
                                work = re.findall(r'([0-9])', work.text)
                                worke = worke.join(work)
                                worke = int(worke)
                                c_name = re.findall(r"(.*)\s", name.text, re.MULTILINE)
                                car_name = ''
                                for z in c_name:
                                    car_name += str(z).strip()
                                x = year.text.strip()
                                pd = ''
                                for w in x:
                                    if str(w).isdigit():
                                        pd += w

                                # calculate age of car
                                if int(pd) > 1900:
                                    age = int(today[0]) - int(pd)
                                elif int(pd) <= 1900:
                                    age = today_jalali['jy'] - int(pd)
                                self.record_counter += 1
                                '''set SQL Query'''
                                query = f'INSERT INTO {table_name} ({fields[0]}, {fields[1]}, {fields[2]},{fields[3]}, {fields[4]}, {fields[6]}) VALUES("{car_name}", {worke}, {toman}, {pd}, "{p_city}", {age});'
                                cursor.execute(query)
                                cnx.commit()
                                print(f'insert into DB{self.record_counter}')
            elif self.c == 2:
                for i in range(1, isfahan):
                    bama_url = f'{first_bama_url}&page={i}'
                    print(bama_url)
                    page_request = requests.get(bama_url)
                    soup = BeautifulSoup(page_request.text, 'html.parser')
                    p_cost = soup.find_all('p', {'class': 'cost'})  # contain cost of car
                    p_work = soup.find_all('p', {'class': 'price hidden-xs'})  # contain work of car
                    h2_name = soup.find_all('h2', {'class': 'persianOrder'})
                    span_pd = soup.find_all('span', {'class': 'price year-label hidden-xs'})
                    # p_city = soup.find_all('span', {'class': 'provice-mobile'})
                    p_city = re.findall(r'province=(.+)&', first_bama_url)[0]

                    for cost, work, name, year in zip(p_cost, p_work, h2_name, span_pd):
                        if des in cost.text.strip() or pre_sel in cost.text.strip() or agree in cost.text.strip() or draft in cost.text.strip() or work.text.strip() == '-' or work.text.strip() == kartx:
                            print('بدونه قیمت یا کارکرد مشخص')
                            pass

                        else:
                            worke = ''
                            T = re.search(r'(.+\d)', cost.text).group(1)
                            toman = ''
                            for n in T:
                                if n.isdigit():
                                    toman += n
                            toman = int(toman)
                            if work.text.strip() == zero:
                                work = '0'
                                work = int(work)
                                c_name = re.findall(r"(.*)\s", name.text, re.MULTILINE)
                                car_name = ''
                                for z in c_name:
                                    car_name += str(z).strip()
                                x = year.text.strip()
                                pd = ''
                                for w in x:
                                    if str(w).isdigit():
                                        pd += w
                                # calculate age of car
                                if int(pd) > 1900:
                                    age = int(today[0]) - int(pd)
                                elif int(pd) <= 1900:
                                    age = today_jalali['jy'] - int(pd)
                                self.record_counter += 1
                                '''set SQL Query'''
                                query = f'INSERT INTO {table_name} ({fields[0]}, {fields[1]}, {fields[2]},{fields[3]}, {fields[4]}, {fields[6]}) VALUES("{car_name}", {work}, {toman}, {pd}, "{p_city}", {age});'
                                cursor.execute(query)
                                cnx.commit()
                                print(f'insert into DB{self.record_counter}')
                            else:
                                work = re.findall(r'([0-9])', work.text)
                                worke = worke.join(work)
                                worke = int(worke)
                                c_name = re.findall(r"(.*)\s", name.text, re.MULTILINE)
                                car_name = ''
                                for z in c_name:
                                    car_name += str(z).strip()
                                x = year.text.strip()
                                pd = ''
                                for w in x:
                                    if str(w).isdigit():
                                        pd += w

                                # calculate age of car
                                if int(pd) > 1900:
                                    age = int(today[0]) - int(pd)
                                elif int(pd) <= 1900:
                                    age = today_jalali['jy'] - int(pd)
                                self.record_counter += 1
                                '''set SQL Query'''
                                query = f'INSERT INTO {table_name} ({fields[0]}, {fields[1]}, {fields[2]},{fields[3]}, {fields[4]}, {fields[6]}) VALUES("{car_name}", {worke}, {toman}, {pd}, "{p_city}", {age});'
                                cursor.execute(query)
                                cnx.commit()
                                print(f'insert into DB{self.record_counter}')
            elif self.c == 3:
                for i in range(1, alborz):
                    bama_url = f'{first_bama_url}&page={i}'
                    print(bama_url)
                    page_request = requests.get(bama_url)
                    soup = BeautifulSoup(page_request.text, 'html.parser')
                    p_cost = soup.find_all('p', {'class': 'cost'})  # contain cost of car
                    p_work = soup.find_all('p', {'class': 'price hidden-xs'})  # contain work of car
                    h2_name = soup.find_all('h2', {'class': 'persianOrder'})
                    span_pd = soup.find_all('span', {'class': 'price year-label hidden-xs'})
                    # p_city = soup.find_all('span', {'class': 'provice-mobile'})
                    p_city = re.findall(r'province=(.+)&', first_bama_url)[0]

                    for cost, work, name, year in zip(p_cost, p_work, h2_name, span_pd):
                        if des in cost.text.strip() or pre_sel in cost.text.strip() or agree in cost.text.strip() or draft in cost.text.strip() or work.text.strip() == '-' or work.text.strip() == kartx:
                            print('بدونه قیمت یا کارکرد مشخص')
                            pass

                        else:
                            worke = ''
                            T = re.search(r'(.+\d)', cost.text).group(1)
                            toman = ''
                            for n in T:
                                if n.isdigit():
                                    toman += n
                            toman = int(toman)
                            if work.text.strip() == zero:
                                work = '0'
                                work = int(work)
                                c_name = re.findall(r"(.*)\s", name.text, re.MULTILINE)
                                car_name = ''
                                for z in c_name:
                                    car_name += str(z).strip()
                                x = year.text.strip()
                                pd = ''
                                for w in x:
                                    if str(w).isdigit():
                                        pd += w
                                # calculate age of car
                                if int(pd) > 1900:
                                    age = int(today[0]) - int(pd)
                                elif int(pd) <= 1900:
                                    age = today_jalali['jy'] - int(pd)
                                self.record_counter += 1
                                '''set SQL Query'''
                                query = f'INSERT INTO {table_name} ({fields[0]}, {fields[1]}, {fields[2]},{fields[3]}, {fields[4]}, {fields[6]}) VALUES("{car_name}", {work}, {toman}, {pd}, "{p_city}", {age});'
                                cursor.execute(query)
                                cnx.commit()
                                print(f'insert into DB{self.record_counter}')
                            else:
                                work = re.findall(r'([0-9])', work.text)
                                worke = worke.join(work)
                                worke = int(worke)
                                c_name = re.findall(r"(.*)\s", name.text, re.MULTILINE)
                                car_name = ''
                                for z in c_name:
                                    car_name += str(z).strip()
                                x = year.text.strip()
                                pd = ''
                                for w in x:
                                    if str(w).isdigit():
                                        pd += w

                                # calculate age of car
                                if int(pd) > 1900:
                                    age = int(today[0]) - int(pd)
                                elif int(pd) <= 1900:
                                    age = today_jalali['jy'] - int(pd)
                                self.record_counter += 1
                                '''set SQL Query'''
                                query = f'INSERT INTO {table_name} ({fields[0]}, {fields[1]}, {fields[2]},{fields[3]}, {fields[4]}, {fields[6]}) VALUES("{car_name}", {worke}, {toman}, {pd}, "{p_city}", {age});'
                                cursor.execute(query)
                                cnx.commit()
                                print(f'insert into DB{self.record_counter}')

            else:
                for i in range(1, 15):
                    bama_url = f'{first_bama_url}&page={i}'
                    print(bama_url)
                    page_request = requests.get(bama_url)
                    soup = BeautifulSoup(page_request.text, 'html.parser')
                    p_cost = soup.find_all('p', {'class': 'cost'})  # contain cost of car
                    p_work = soup.find_all('p', {'class': 'price hidden-xs'})  # contain work of car
                    h2_name = soup.find_all('h2', {'class': 'persianOrder'})
                    span_pd = soup.find_all('span', {'class': 'price year-label hidden-xs'})
                    # p_city = soup.find_all('span', {'class': 'provice-mobile'})
                    p_city = re.findall(r'province=(.+)&', first_bama_url)[0]

                    for cost, work, name, year in zip(p_cost, p_work, h2_name, span_pd):
                        if des in cost.text.strip() or pre_sel in cost.text.strip() or agree in cost.text.strip() or draft in cost.text.strip() or work.text.strip() == '-' or work.text.strip() == kartx:
                            print('بدونه قیمت یا کارکرد مشخص')
                            pass

                        else:
                            worke = ''
                            T = re.search(r'(.+\d)', cost.text).group(1)
                            toman = ''
                            for n in T:
                                if n.isdigit():
                                    toman += n
                            toman = int(toman)
                            if work.text.strip() == zero:
                                work = '0'
                                work = int(work)
                                c_name = re.findall(r"(.*)\s", name.text, re.MULTILINE)
                                car_name = ''
                                for z in c_name:
                                    car_name += str(z).strip()
                                x = year.text.strip()
                                pd = ''
                                for w in x:
                                    if str(w).isdigit():
                                        pd += w
                                # calculate age of car
                                if int(pd) > 1900:
                                    age = int(today[0]) - int(pd)
                                elif int(pd) <= 1900:
                                    age = today_jalali['jy'] - int(pd)
                                self.record_counter += 1
                                '''set SQL Query'''
                                query = f'INSERT INTO {table_name} ({fields[0]}, {fields[1]}, {fields[2]},{fields[3]}, {fields[4]}, {fields[6]}) VALUES("{car_name}", {work}, {toman}, {pd}, "{p_city}", {age});'
                                cursor.execute(query)
                                cnx.commit()
                                print(f'insert into DB{self.record_counter}')
                            else:
                                work = re.findall(r'([0-9])', work.text)
                                worke = worke.join(work)
                                worke = int(worke)
                                c_name = re.findall(r"(.*)\s", name.text, re.MULTILINE)
                                car_name = ''
                                for z in c_name:
                                    car_name += str(z).strip()
                                x = year.text.strip()
                                pd = ''
                                for w in x:
                                    if str(w).isdigit():
                                        pd += w

                                # calculate age of car
                                if int(pd) > 1900:
                                    age = int(today[0]) - int(pd)
                                elif int(pd) <= 1900:
                                    age = today_jalali['jy'] - int(pd)
                                self.record_counter += 1
                                '''set SQL Query'''
                                query = f'INSERT INTO {table_name} ({fields[0]}, {fields[1]}, {fields[2]},{fields[3]}, {fields[4]}, {fields[6]}) VALUES("{car_name}", {worke}, {toman}, {pd}, "{p_city}", {age});'
                                cursor.execute(query)
                                cnx.commit()
                                print(f'insert into DB{self.record_counter}')

run = Data_fetch()
run.fetch_data()
print('final record= ', run.record_counter)
cursor.close()
cnx.close()
end = datetime.now()
print('time = ',end - start)