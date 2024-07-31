from sqlalchemy.orm import Session

from models import Chat_Log

from passlib.context import CryptContext


def create_log(family_id: str, content: str, db: Session):
    log = Chat_Log(
        role = "user",
        family_id = family_id,
        content = content
    )
    db.add(log)
    db.commit()
    db.refresh(log)
    learned_data = db.query(Chat_Log).filter(
        Chat_Log.family_id == family_id,
    ).all()
    return learned_data