from sqlalchemy.orm import Session

from models import Family, User
from CLOVA_Chatbot import log_crud

def get_family(id: str, db: Session):  
    return db.query(Family).filter(Family.id == id).first()


def create_Family(random_string: str, db: Session, phone: str):
    family = Family(
        id =random_string,
    )
    db.add(family)
    user = db.query(User).filter(User.phone == phone).first()
    user.family_id = random_string
    db.commit()

    content = f"{user.user_name}에 대한 간단한 정보: \n 생년월일: {user.birth} \n 성별: {user.sex}"
    log_crud.create_log(user.family_id,content, db)

    return family


def join_Family(id: str, phone: str, db: Session):

    user = db.query(User).filter(User.phone == phone).first()
    user.family_id = id
    db.commit()

    content = f"{user.user_name}에 대한 간단한 정보: \n{user}"
    log_crud.create_log(user.family_id,content, db)
    return id

def get_cnt(family_id: str, db: Session):  
    return db.query(User).filter(User.family_id == family_id).count()