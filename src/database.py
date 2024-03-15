
from sqlalchemy import create_engine
from os import getenv

from sqlalchemy import text

DB_USER = getenv('POSTGRES_USER')
DB_PASSWORD = getenv('POSTGRES_PASSWORD')
DB_NAME = getenv('POSTGRES_DB')

DB_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@db:5432/{DB_NAME}'

engine = create_engine(DB_URL)


def check_db_connection():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1;"))
        for row in result:
            print(row)
    pass

def db_first_router_function():
    check_db_connection()
    pass

def db_second_router_function():
    check_db_connection()
    pass
