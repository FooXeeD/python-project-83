from sqlalchemy import Column
from page_analyzer.models.basemodel import BaseModel
from sqlalchemy import VARCHAR

class Urls(BaseModel):
    __tablename__ = 'urls'

    name = Column(VARCHAR(255), nullable=False)# noqa