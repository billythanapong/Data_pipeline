# pip install psycopg2

import psycopg2 as p2
import pandas as pd



class pg_connect:

    def __init__(self) :
        try:
            # Seeking host (can be i.p. or localhost), user by 
            self.connect =  p2.connect(host = 'localhost',database = 'postgres',user= 'Billy', password= '123T123+')
            # To point to the connection
            self.cursor = self.connect.cursor()
            print(f'Connected:{self.connect}')
        except:
            print('Cannot connect to Pgadmin')

    def execute(self,sql_command,*args):
        self.cursor.execute(sql_command)
        return print('Complete')

    
    def closing(self):
        # Closing cursor and connection
        self.connect.commit()
        self.connect.close()
        self.cursor.close()


# Test connection -- Pass!
# print(connect)


# Define sql function


# cursor.execute("create table sample(id serial primary key, menu varchar , price int);")
# cursor.execute('insert into sample(menu,price) values(%s,%s)',('water',15))

# cursor.execute("select * from sample;")




# print(cursor.fetchall())

