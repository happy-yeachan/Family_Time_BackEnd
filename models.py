from sqlalchemy import Column, Integer, VARCHAR, DateTime, ForeignKey, Float, create_engine, or_
from datetime import datetime
from sqlalchemy.orm import relationship


from database import Base

class User(Base):
  __tablename__ = "Users"

  user_name = Column(VARCHAR(10), nullable=False)
  phone= Column(VARCHAR(100), primary_key=True, nullable=False, unique=True)
  birth= Column(VARCHAR(100), nullable=False)
  sex=Column(VARCHAR(20), nullable=False)
  hashed_pw=Column(VARCHAR(100), nullable=False)
  family_id = Column(VARCHAR(20), ForeignKey('Families.id'), default="None") 
  regdate = Column(DateTime, nullable=False, default=datetime.now)


class Family(Base):
  __tablename__ = 'Families'
    
  id = Column(VARCHAR(20), primary_key=True)


class Family_Photo(Base):
    __tablename__ = 'photos'

    photo_no = Column(Integer, primary_key=True, autoincrement=True)
    file = Column(VARCHAR, nullable=False)
    author = Column(VARCHAR(10), nullable=False)
    regdate = Column(DateTime, nullable=False, default=datetime.now)
    family_id = Column(VARCHAR(20), ForeignKey('Families.id'), default="None") 
    comment = Column(VARCHAR(20), nullable=True, default="None")
    sentiment = Column(VARCHAR(20), nullable=False)

    # 댓글 관계 추가
    comments = relationship("Family_Photo_comment", back_populates="photo")

class Family_Photo_comment(Base):
    __tablename__ = 'photo_comments'

    comment_id = Column(Integer, primary_key=True, autoincrement=True)  # 댓글 ID
    photo_no = Column(VARCHAR, ForeignKey('photos.photo_no'), nullable=False)  # 댓글이 달린 사진의 파일명
    user_name = Column(Integer, ForeignKey('Users.user_name'), nullable=False)  # 댓글 작성자
    comment = Column(VARCHAR(255), nullable=False)  # 댓글 내용
    regdate = Column(DateTime, nullable=False, default=datetime.now)  # 댓글 작성일

    # 관계 설정 (옵션)
    photo = relationship("Family_Photo", back_populates="comments")
    user = relationship("User")

class Chat_Log(Base):
    __tablename__ = 'chat_log'

    log_id = Column(Integer, primary_key=True, autoincrement=True)  # ID
    role = Column(VARCHAR(20), nullable=False)  
    content = Column(VARCHAR(255), nullable=False) 
    family_id = Column(VARCHAR(20), ForeignKey('Families.id'), default="None") 

