from sqlalchemy.orm import Base

class BaseModel(Base):
    __abstract__ = True
    
    id = Column(Integer, nallable=False, unique=True,primary_key=True, autoincrement=True)
    created_at = Column(TIMESTAMP,nullable=False)
