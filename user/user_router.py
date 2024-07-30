
from sqlalchemy.orm import Session
from database import get_db

from datetime import datetime
from datetime import timedelta
from jose import jwt, JWTError

from fastapi import APIRouter, Depends, status, HTTPException, Response, Request
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

from user import user_schema, user_crud

import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = float(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

app = APIRouter(
  prefix="/user"
)

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(request: Request, db: Session = Depends(get_db)):
    token = request.cookies.get('access_token')
    
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )


    try:
        if token is None:
            raise credentials_exception

        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        phone: str = payload.get("sub")
        if phone is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception
    
    user = user_crud.get_user(phone, db)
    if user is None:
        raise credentials_exception
    
    return user

@app.post(path="/signup")
async def signup(new_user: user_schema.NewUserForm, db: Session = Depends(get_db)):    
    # 회원 존재 여부 확인
    user = user_crud.get_user(new_user.phone, db)

    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists")

    # 회원 가입
    user_crud.create_user(new_user, db)

    return HTTPException(status_code=status.HTTP_200_OK, detail="Signup successful")


@app.post(path="/login")
async def login(response: Response, login_form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # 회원 존재 여부 확인
    user = user_crud.get_user(login_form.username, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid user or password")
    
    # 로그인
    res = user_crud.verify_password(login_form.password, user.hashed_pw)

    # 토큰 생성
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.phone}, expires_delta=access_token_expires)

    # 쿠키에 저장
    response.set_cookie(key="access_token", value=access_token, expires=access_token_expires, httponly=True)

    if not res:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid user or password")

    return user_schema.Token(access_token=access_token, token_type="bearer"), user_schema.Current_User(user_name=user.user_name, phone=user.phone, birth=user.birth, family_id=user.family_id)


@app.get(path="/logout")
async def logout(response: Response):

    # 쿠키 삭제
    response.delete_cookie(key="access_token")

    return HTTPException(status_code=status.HTTP_200_OK, detail="Logout successful")

@app.get("/me", response_model=user_schema.Current_User)
async def read_users_me(current_user: user_schema.Current_User = Depends(get_current_user)):
    return current_user