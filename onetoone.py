from sqlalchemy import create_engine

DB_USER = 'postgres'
DB_PASSWORD = 'secret'
DB_NAME = 'test'
DB_ECHO = True
engine = create_engine(
        f'postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}',
        echo=True,
    )

