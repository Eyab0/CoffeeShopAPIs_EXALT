from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config import config
from models.models import Base
from contextlib import contextmanager

DATABASE_URI = f"postgresql+psycopg2://postgres:{config.PASSWORD}@{config.HOST}:5432/{config.DBNAME}"
engine = create_engine(DATABASE_URI)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
sess = Session()


@contextmanager
def session_scope():
    try:
        yield sess
        sess.commit()
    except Exception:
        sess.rollback()
        sess.close()
        raise
