import mysql.connector


class DB_manager(object):
    def __init__(self,):

        """set connection"""
        self.cnx = mysql.connector.connect(user='mejomba',
                                           password='09360521688',
                                           host='127.0.0.1',
                                           database='maktabkhone')

        self.cursor = self.cnx.cursor()
        print('connected to ', self.cnx.database, 'with user', self.cnx.user)

        '''initial parameter'''
        self.table_name = 'cars'
        self.fields = ['name', 'work', 'price', 'pd', 'city', 'id', 'age']

    def get_record(self):
        """ retrieve data from DB & send to ML """

        query = f"SELECT {self.fields[0]},{self.fields[1]},{self.fields[2]},{self.fields[3]},{self.fields[4]},{self.fields[6]} FROM {self.table_name};"
        self.cursor.execute(query)
        x = self.cursor.fetchall()
        with open('data.csv', 'w', encoding='utf-8')as f:
            for n in x:
                f.write(f"{n[0]},{n[1]},{n[4]},{n[5]},{n[2]},{n[3]}\n")

    def clear_db(self):
        """ clear data base from duplicated record's """
        self.query = f"DELETE t1 FROM car2 t1 INNER JOIN cars t2 WHERE t1.id<t2.id and t1.price=t2.price and t1.city=t2.city and t1.name=t2.name and t1.work=t2.work and t1.pd=t2.pd and t1.age=t2.age;"
        self.cursor.execute(self.query)
        self.cnx.commit()
        print("database clean")

    def close_cnx(self):
        self.cursor.close()
        self.cnx.close()


manager = DB_manager()
manager.clear_db()
manager.get_record()


