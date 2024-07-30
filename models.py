from sqlalchemy import Column, Integer, VARCHAR, DateTime, ForeignKey, Float
from datetime import datetime

from database import Base

class User(Base):
  __tablename__ = "Users"
  
  user_no = Column(Integer, primary_key=True, autoincrement=True)
  user_name = Column(VARCHAR(10), nullable=False)
  phone= Column(VARCHAR(100), nullable=False, unique=True)
  birth= Column(VARCHAR(100), nullable=False, unique=True)
  hashed_pw=Column(VARCHAR(100), nullable=False)
  role=Column(VARCHAR(20), nullable=False, default='MEMBER')
  family_id = Column(VARCHAR(20), ForeignKey('Families.id'), default="None") 
  regdate = Column(DateTime, nullable=False, default=datetime.now)


class Family(Base):
  __tablename__ = 'Families'
    
  id = Column(VARCHAR(20), primary_key=True)
  family_name = Column(VARCHAR(20), nullable=False)


class Family_Photo(Base):
  __tablename__ = 'photos'

  file = Column(VARCHAR, nullable=False, primary_key=True)
  author = Column(VARCHAR(10), nullable=False)
  regdate = Column(DateTime, nullable=False, default=datetime.now)
  family_id = Column(VARCHAR(20), ForeignKey('Families.id'), default="None") 
  comment = Column(VARCHAR(20), nullable=True, default="None")
  positive = Column(Float, default=0)
  negative = Column(Float, default=0)