import mysql.connector




class DB_manager(object):
    def __init__(self,):

        """set connection"""
        self.cnx = mysql.connector.connect(user='mejomba',
                                      password='09360521688',
                                      host='127.0.0.1',
                                      database='maktabkhone'
                                      )
        self.cursor = self.cnx.cursor()
        print('connected to ', self.cnx.database, 'with user', self.cnx.user)

        '''initial parameter'''
        self.table_name = 'cars'
        self.fields = ['name', 'work', 'price', 'pd', 'city', 'id']

       #create table if not exist
    '''try:
            self.cursor.execute(f'CREATE TABLE {self.table_name} ({self.fields[0]} char(50), {self.fields[1]} int, {self.fields[2]} int,'
                           f' {self.fields[3]} char(20), {self.fields[4]} int);')
            print(f'table {self.table_name} created.')
        except:
            print(f'some thing wrong OR table {self.table_name} already exists.')'''


    def insert_into(self):
        """ get ARRAY from 'data_fech.Data_fetch.fetch_data & insert into DB' """
        pass

    def get_record(self):
        """ retrieve data from DB & send to ML """
        pass

    def clear_db(self):
        """ clear data base from duplicated record's """
        '''ALTER IGNORE TABLE jobs
ADD UNIQUE INDEX idx_name (site_id, title, company);

['name', 'work', 'price', 'pd', 'city', 'id']'''
        self.query = f"DELETE t1 FROM cars t1 INNER JOIN cars t2 WHERE t1.id<t2.id and t1.price=t2.price and t1.city=t2.city and t1.name=t2.name and t1.work=t2.work and t1.pd=t2.pd and t1.age=t2.age;"
        self.cursor.execute(self.query)
        self.cnx.commit()
        print("database clean")
        pass

    def close_cnx(self):
        self.cursor.close()
        self.cnx.close()


manager = DB_manager()
manager.clear_db()
manager.close_cnx()

