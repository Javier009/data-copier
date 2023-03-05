import pandas as pd
from sqlalchemy import create_engine, text
import os

#Validating that the table exists in the data base
def main():
    query = 'SELECT * FROM orders LIMIT 10'
    engine = create_engine('postgresql://retail_user:itversity@localhost:5452/retail_db')

    with engine.begin() as conn:
        try:
            pd.read_sql_query(sql=text(query), con=conn)
            print('Table exists and has been converted to a pandas data frame')
        except:
            print('Table does not exists')

    # Reading JSON data
    BASE_DIR = '/Users/delgadonoriega/Desktop/Research/data/retail_db_json'
    table_name='orders'

    file_name = os.listdir(f'{BASE_DIR}/{table_name}')[0]
    fp =  f'{BASE_DIR}/{table_name}/{file_name}'

    # --> READING THE DATA IN CHUNKS
    json_reader = pd.read_json(fp, lines=True, chunksize=1000)

    # Populating SQL table in our retail_db database

    for df in json_reader:
        min_key = df['order_id'].min()
        max_key = df['order_id'].max()

        with engine.begin() as conn:
            df.to_sql(table_name, conn, if_exists='append', index=False)
            print(f'Added data from order_id: {min_key} to {max_key}')
    print('Data added successfully')


if __name__ == '__main__':
    main()

