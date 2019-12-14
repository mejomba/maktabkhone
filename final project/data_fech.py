from bs4 import BeautifulSoup
import re
import requests



zero = 'کارکرد صفر'
des = 'در توضیحات'
agree = 'توافقی'
draft = 'حواله'
pre = 'پیش'
pre_sel = 'پیش فروش'
toman  = 'تومان'

class Data_fetch(object):
    def __init__(self):
        pass

    def search(self, search_input):
        """get search query from user & search in google for find target URL"""
        pass

    def fetch_data(self):
        """grt URL from 'search' & fetch data while 150 record fetched
        send ARRAY to DB_manager for insert into database"""
        for i in range(1, 3):
            bama_url = f'https://bama.ir/car/all-brands/all-models/all-trims?page={i}'
            print(bama_url)
            page_request = requests.get(bama_url)
            soup = BeautifulSoup(page_request.text, 'html.parser')
            p_cost = soup.find_all('p', {'class': 'cost'})  # contain cost of car
            p_work = soup.find_all('p', {'class': 'price hidden-xs'})  # contain work of car
            h2_name = soup.find_all('h2', {'class': 'persianOrder'})
            span_pd = soup.find_all('span', {'class': 'price year-label hidden-xs'})

            for cost, work, name, year in zip(p_cost, p_work, h2_name, span_pd):
                if des in cost.text.strip() or pre_sel in cost.text.strip() or agree in cost.text.strip() or draft in cost.text.strip() or work.text.strip() == '-':
                    #print('بدونه قیمت یا کارکرد مشخص')
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
                        pd = year.text.strip()
                        print(f'name= {car_name}, cost=  {toman}, work=  {work}, pd= {pd}')
                        #return f"INSERT INTO {table_name} ({o.fields[0]}, {fields[1]}) values ('{toman}', '{work}');"
                    else:
                        work = re.findall(r'([0-9])', work.text)
                        worke = worke.join(work)
                        worke = int(worke)
                        c_name = re.findall(r"(.*)\s", name.text, re.MULTILINE)
                        car_name = ''
                        for z in c_name:
                            car_name += str(z).strip()
                        x = year.text.strip()
                        for w in x:
                            if str(x).isdigit():

                        print(f'name= {car_name}, cost=  {toman}, work=  {worke}, pd= {pd}')
                        #query = f"INSERT INTO {table_name} ({fields[0]}, {fields[1]}) values ('{toman}', '{worke}');"

run = Data_fetch()
run.fetch_data()