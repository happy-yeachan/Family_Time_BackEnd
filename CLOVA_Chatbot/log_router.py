from sqlalchemy.orm import Session
from database import get_db

from fastapi import APIRouter, Depends, status, HTTPException, Response, Request, UploadFile
from jose import jwt, JWTError
from user import user_router, user_crud
from CLOVA_Chatbot import log_crud, chatbot

app = APIRouter(
  prefix="/chatbot"
)
def get_current(request: Request, db: Session = Depends(get_db)):
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
    user = user_crud.get_user(phone, db)
    if user is None:
        raise credentials_exception
    return user

@app.post(path="/chat")
async def upload(content: str,  db: Session = Depends(get_db), user_data: dict = Depends(get_current)): 
    learned_datas = log_crud.create_log(user_data.family_id,f"{content}", db)
    log = [{"role": learned_data.role, "content": learned_data.content} for learned_data in learned_datas]
    return chatbot.call_clova(log)

@app.post(path="/ask")
async def upload(question: str, answer:str,  db: Session = Depends(get_db), user_data: dict = Depends(get_current)): 
    content = f"{question}에 대한 {user_data.user_name}의 답변 = {answer}"
    learned_datas = log_crud.create_log(user_data.family_id,content, db)
    return HTTPException(status_code=status.HTTP_200_OK, detail="successful")

