def load_db_table(df, db, table_name, key):
    from sqlalchemy import create_engine, text
    min_key = df[key].min()
    max_key = df[key].max()

    # Initializing connection and appending data to the table
    engine = create_engine(db)
    with engine.begin() as conn:
        df.to_sql(table_name, conn, if_exists='append', index=False)  # If the table does not exists it will create a new one
        print(f'Loaded data for {table_name} within the range of {min_key} and {max_key}')


if __name__ == '__main__':
    import pandas as pd
    import os
    from sqlalchemy import create_engine, text

    data = [{'user_id': 1, 'user_first_name': 'Scott', 'user_last_name': 'Tiger'},
            {'user_id': 2, 'user_first_name': 'Donald', 'user_last_name': 'Duck'}]
    df = pd.DataFrame(data)
    configs = dict(os.environ.items())
    # db = 'postgresql://retail_user:itversity@localhost:5452/retail_db'
    db = f'postgresql://{configs["DB_USER"]}:{configs["DB_PASS"]}@{configs["DB_HOST"]}:{configs["DB_PORT"]}/{configs["DB_NAME"]}'
    table_name = 'users'
    key = 'user_id'
    load_db_table(df, db, 'users', 'user_id')



