from sqlalchemy import TIMESTAMP
from sqlalchemy import Column, Integer
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, nullable=False, unique=True,
                primary_key=True, autoincrement=True)
    created_at = Column(TIMESTAMP, nullable=False)  # noqa
