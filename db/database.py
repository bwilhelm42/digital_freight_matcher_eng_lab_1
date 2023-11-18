import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Base

engine = create_engine(os.getenv('DATABASE_URL'))
Session = sessionmaker(bind=engine)


def create_tables():
    Base.metadata.create_all(engine)


def get_session():
    return Session()


def get_db():
    db = get_session()
    try:
        yield db
    finally:
        db.close()
