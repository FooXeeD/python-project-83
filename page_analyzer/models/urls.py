class Urls(BaseModel):
    __tablename__ = 'urls'

    name = Column(VARCHAR(255), nullable=False)
    