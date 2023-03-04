import os
import sys
#importing functions needed to integreate json data read and sql write
from read import get_json_reader
from write import load_db_table

def process_table(BASE_DIR,conn, table_name):
    #Data read
    json_reader = get_json_reader(BASE_DIR, table_name)  # returns an iterable object composed of data frames
    # Data injection
    for df in json_reader:
        load_db_table(df, conn, table_name, df.columns[0])  # load the data in chunks

def main():
    # Data reading section
    configs = dict(os.environ.items())
    BASE_DIR = configs['BASE_DIR']
    table_names = input('Please add a table names available in the docker container separated by a comma: ')
    table_names = table_names.split(',')
    # Data injection into tables
    db = f'postgresql://{configs["DB_USER"]}:{configs["DB_PASS"]}@{configs["DB_HOST"]}:{configs["DB_PORT"]}/{configs["DB_NAME"]}'
    for table_name in table_names:
        process_table(BASE_DIR=BASE_DIR, conn=db, table_name=table_name)

if __name__ == '__main__':
    main()


# --> BASE_DIR = os.environ.get('BASE_DIR')
# -->  table_name = os.environ.get('TABLE_NAME')
# --> table_name = configs['TABLE_NAME']