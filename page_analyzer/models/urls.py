from sqlalchemy import Column
from page_analyzer.models import BaseModel

class Urls(BaseModel):
    __tablename__ = 'urls'

    name = Column(VARCHAR(255), nullable=False)