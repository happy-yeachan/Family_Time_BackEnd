from sqlalchemy.orm import Session

from models import Family, User


def get_family(id: str, db: Session):  
    return db.query(Family).filter(Family.id == id).first()


def create_Family(random_string: str, name: str, db: Session, phone: str):
    family = Family(
        id =random_string,
        family_name=name,
    )
    db.add(family)
    user = db.query(User).filter(User.phone == phone).first()
    user.family_id = random_string
    db.commit()
    return family


def join_Family(id: str, phone: str, db: Session):

    user = db.query(User).filter(User.phone == phone).first()
    user.family_id = id
    db.commit()
    return id