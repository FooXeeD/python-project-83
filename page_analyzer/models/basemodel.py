from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import declarative_base
import os
from sqlalchemy import TIMESTAMP

DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(DATABASE_URL)

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    created_at = Column(TIMESTAMP,nullable=False)# noqa
