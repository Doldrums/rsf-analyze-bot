from os import environ

DB_USER = environ.get("POSTGRES_USER")
DB_PASSWORD = environ.get("POSTGRES_PASSWORD")
DB_DB = environ.get("POSTGRES_DB")
DB_PORT = environ.get("POSTGRES_PORT")
DB_HOST = environ.get("POSTGRES_HOST")
DB_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DB}"
)
KAFKA_HOST = environ.get("KAFKA_HOST")
KAFKA_PORT = environ.get("KAFKA_PORT")
