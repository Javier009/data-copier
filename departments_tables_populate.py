import pandas as pd
from sqlalchemy import create_engine, text
import os

#Validating that the table exists in the data base

query = 'SELECT * FROM departments'
engine = create_engine('postgresql://retail_user:itversity@localhost:5452/retail_db')

with engine.begin() as conn:
    pd.read_sql_query(sql=text(query), con=conn)

#Reading JSON data
BASE_DIR = '/Users/delgadonoriega/Desktop/Research/data/retail_db_json'
table_name='departments'

file_name = os.listdir(f'{BASE_DIR}/{table_name}')[0]
fp =  f'{BASE_DIR}/{table_name}/{file_name}'

df = pd.read_json(fp, lines=True)

#Populating SQL table departments with Pandas
with engine.begin() as conn:
    df.to_sql('departments', conn, if_exists='append', index=False)

