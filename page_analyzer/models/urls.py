from sqlalchemy import Column
from sqlalchemy import VARCHAR

from page_analyzer.models.basemodel import BaseModel


class Urls(BaseModel):
    __tablename__ = 'urls'

    name = Column(VARCHAR(255), nullable=False)  # noqa
