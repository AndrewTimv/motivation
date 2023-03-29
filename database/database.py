from sqlalchemy import create_engine, URL

db_url = URL.create(
    'sqlite',
    database='motivation.db'
)

engine = create_engine(db_url)
