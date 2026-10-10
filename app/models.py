from sqlalchemy import Column, Integer, String,Float
from datetime import datetime
from .database import Base

class Good(Base):
    __tablename__ = "goods"
    id = Column(Integer,primary_key=True,index=True)
    gname = Column(String(20),nullable=False)
    price = Column(Float,nullable=False)
    stock = Column(Integer,nullable=False,default=0)
