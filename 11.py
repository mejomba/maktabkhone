import re
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
    print(f'some thing wrong OR table {table_name} is now exists.')

'''set pattern'''
mail_pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
password_pattern = r'[A-Za-z0-9]{8,}'

'''this code only insert one record to database if you won't insert multiple record update "while" condition 
or change loop structure'''
connected = True
while connected:
    email = input('email: ')
    password = input('password: ')
    if not re.match(mail_pattern, email):
        print(f'{email} is not a valid email address\nvalid email--> "expression@string.string"')
    elif not re.match(password_pattern, password):
        print("password must be 8 character contain digit's & letter's")
    else:
        query = f"INSERT INTO {table_name} values('{email}','{password}');"
        cursor.execute(query)
        cnx.commit()
        cursor.close()
        cnx.close()
        connected = False
