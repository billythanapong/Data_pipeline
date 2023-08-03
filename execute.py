import pandas as pd
from conn import pg_connect
import json




# Read json data
with open('example_2.json','r') as file :
      json_data = json.load(file)
      print(json_data)



data_list = []
for subject, question in json_data['quiz'].items():
    for q_num, q_details in question.items():
        question = q_details['question']
        choices = q_details['options']
        answer = q_details['answer']

        for choice in choices:
            data_list.append((subject, q_num, question, choice, answer))




pg = pg_connect()


# pg.execute('create table test2(id serial primary key, subject varchar, qnum varchar,question varchar, options varchar,answer varchar );')


for i in data_list:
    print(len(i))
    pg.execute(f"INSERT INTO test2 (subject, qnum, question, options, answer) VALUES (%s, %s, %s, %s, %s);", (i[0], i[1], i[2], i[3], i[4]))



pg.closing()


df = pd.read_sql('select * from test2', pg.connect)
print(df.head())


# # df = pd.read_sql('select * from test2',pg)
# # df.head()



# # df  = pg.execute_command('select * from sample')
# # pg.closing()



# # pd.read_sql(,con)