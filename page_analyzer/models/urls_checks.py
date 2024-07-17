from sqlalchemy import Column, Integer, ForeignKey
from page_analyzer.models.basemodel import BaseModel
from sqlalchemy import VARCHAR, TEXT

class Urls_checks(BaseModel):
    __tablename__ = 'urls_checks'

    url_id = Column(ForeignKey('urls.id'))
    status_code = Column(Integer)
    h1 = Column(TEXT)# noqa
    title = Column(TEXT)# noqa
    description = Column(TEXT)# noqa


class Urls(BaseModel):
    __tablename__ = 'urls'

    name = Column(VARCHAR(255), nullable=False)# noqa
