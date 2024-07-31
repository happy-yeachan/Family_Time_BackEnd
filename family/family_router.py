
from sqlalchemy.orm import Session
from database import get_db

from fastapi import APIRouter, Depends, status, HTTPException, Response, Request
from jose import jwt, JWTError
from family import family_crud
from user import user_router, user_schema
import random
import string

app = APIRouter(
  prefix="/family"
)

def get_current_phone(request: Request, db: Session = Depends(get_db)):
    token = request.headers.get('access_token')
    
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )


    try:
        if token is None:
            raise credentials_exception

        payload = jwt.decode(token, user_router.SECRET_KEY, algorithms=[user_router.ALGORITHM])
        phone: str = payload.get("sub")
        if phone is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception
    
    return phone

@app.post(path="/create")
async def create_family(db: Session = Depends(get_db), phone: user_schema.Current_User = Depends(get_current_phone)): 
    
    # 존재 여부 확인
    while(True):
        characters = string.ascii_letters + string.digits
        random_string = ''.join(random.choice(characters) for _ in range(5))
        if not family_crud.get_family(random_string, db):
            family_crud.create_Family(random_string, db, phone)
            break


    return random_string



@app.get(path="/join")
async def join(id: str, db: Session = Depends(get_db), phone: user_schema.Current_User = Depends(get_current_phone)):

    if not family_crud.get_family(id, db):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        raise credentials_exception
    
    family_crud.join_Family(id, phone, db)

    return HTTPException(status_code=status.HTTP_200_OK, detail="join successful")

@app.get("/")
async def read_users_me(current_user: user_schema.Current_User = Depends(user_router.get_current_user), db: Session = Depends(get_db)):
    return family_crud.get_cnt(current_user.family_id, db)