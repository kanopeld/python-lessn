from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists

DB_USER = 'postgres'
DB_PASSWORD = 'secret'
DB_NAME = 'test'
DB_ECHO = True
engine = create_engine(
        # "postgresql://postgres:postgres@localhost/test",
        f'postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}',
        echo=True,
    )

if not database_exists(engine.url):
    create_database(engine.url)
