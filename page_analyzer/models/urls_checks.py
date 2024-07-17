from sqlalchemy import Column, Integer, ForeignKey
from page_analyzer.models import BaseModel


class Urls_checks(BaseModel):
    __tablename__ = 'urls_checks'

    url_id = Column(ForeignKey('urls.id'))
    status_code = Column(Integer)
    h1 = Column(TEXT)
    title = Column(TEXT)
    description = Column(TEXT)


class Urls(BaseModel):
    __tablename__ = 'urls'

    name = Column(VARCHAR(255), nullable=False)
