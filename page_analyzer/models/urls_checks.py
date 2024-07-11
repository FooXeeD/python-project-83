class Urls_checks(BaseModel):
    __tablename__ = 'urls_checks'

    url_id = Column(ForeignKey('urls.id'))
    status_code = Column(Integer)
    h1 = Column(TEXT)
    title = Column(TEXT)
    description = Column(TEXT)