import mysql.connector

'''set connection'''
cnx = mysql.connector.connect(user='mejomba',
                              password='09360521688',
                              host='127.0.0.1',
                              database='maktabkhone'
                              )
cursor = cnx.cursor()

'''initial parameter'''
table_name = 'employee'
fields = ['Name', 'Height', 'Weight']

'''set SQL Query'''
query = (f'SELECT {fields[0]}, {fields[1]}, {fields[2]} FROM {table_name} order by {fields[1]} desc, {fields[2]} asc;')
cursor.execute(query)

'''Output'''
for (Name, Height, Weight) in cursor:
    print(f'{Name} {Height} {Weight}')

'''close connection'''
cursor.close()
cnx.close()