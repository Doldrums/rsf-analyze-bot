import logging

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.settings import settings


# db = Database(settings.DB_URL)
# metadata = sqlalchemy.MetaData()
# engine = sqlalchemy.create_engine(settings.DB_URL, pool_size=3, max_overflow=0)
# create_database(engine.url)

# LocalSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# metadata.create_all(engine)
# Base = declarative_base()


engine = create_engine(
    settings.DB_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    """
    A dependency for working with PostgreSQL
    """
    try:
        db = SessionLocal()
        yield db
    except Exception as e:
        logging.error(e)
    finally:
        db.close()
