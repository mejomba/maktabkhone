import mysql.connector


class DB_manager(object):
    def __init__(self,):

        '''set connection'''
        self.cnx = mysql.connector.connect(user='mejomba',
                                      password='09360521688',
                                      host='127.0.0.1',
                                      database='maktabkhone'
                                      )
        self.cursor = self.cnx.cursor()
        print('connected to ', self.cnx.database, 'with user', self.cnx.user)

        '''initial parameter'''
        self.table_name = 'cars'
        self.fields = ['name', 'work', 'price', 'city', 'pd']

        '''create table if not exist'''
        try:
            self.cursor.execute(f'CREATE TABLE {self.table_name} ({self.fields[0]} char(50), {self.fields[1]} int, {self.fields[2]} int,'
                           f' {self.fields[3]} char(20), {self.fields[4]} int);')
            print(f'table {self.table_name} created.')
        except:
            print(f'some thing wrong OR table {self.table_name} already exists.')

        pass

    def insert_into(self):
        """get ARRAY from 'data_fech.Data_fetch.fetch_data & insert into DB'"""
        Data_fetch.fetch_data()
        pass

    def get_record(self):
        """retrieve data from DB & send to ML"""
        pass

x = DB_manager()
