import pandas as pd
from sqlalchemy import create_engine, text
import os
def main():
    users_list = [
        {'user_first_name': 'Scott', 'user_last_name': 'Tiger'},
        {'user_first_name': 'Donald', 'user_last_name': 'Duck'}
    ]
    df = pd.DataFrame(users_list)
    engine = create_engine('postgresql://retail_user:itversity@localhost:5452/retail_db')


    with engine.begin() as conn:
        df.to_sql('users', conn, if_exists='append', index=False)


if __name__ == '__main__':
    main()