import os
def main():
    DB_NAME = os.environ.get('DB_NAME')
    print(f'Hello World form {DB_NAME}')

if __name__ == '__main__':
    main()