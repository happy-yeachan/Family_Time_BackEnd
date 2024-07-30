from sqlalchemy.orm import Session
from database import get_db

from fastapi import APIRouter, Depends, status, HTTPException, Response, Request, UploadFile
from jose import jwt, JWTError
from user import user_router, user_crud
from f_photo import f_photo_crud

app = APIRouter(
  prefix="/photo"
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

@app.post(path="/upload")
async def upload(file: UploadFile, comment: str,  db: Session = Depends(get_db), user_data: dict = Depends(get_current)): 
    f_photo_crud.upload_photo(file, comment, user_data.user_name, user_data.family_id, db)

    return HTTPException(status_code=status.HTTP_200_OK, detail="upload successful")
    
@app.get(path="/all")
async def load_all(db: Session = Depends(get_db), user_data: dict = Depends(get_current)):
    try:
        # 오늘 업로드된 사진 불러오기
        photos = f_photo_crud.load_all_photo(user_data.family_id, db)

        if not photos:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No photos found for today")

        return {
            "status": "success",
            "photos": [{photo.file, photo.photo_no} for photo in photos]  # 파일 경로 리스트 반환
        }

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
@app.get(path="/today")
async def load_today(db: Session = Depends(get_db), user_data: dict = Depends(get_current)):
    try:
        # 오늘 업로드된 사진 불러오기
        photos = f_photo_crud.load_today_photo(user_data.family_id, db)

        if not photos:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No photos found for today")

        return {
            "status": "success",
            "photos": [{photo.file, photo.photo_no} for photo in photos] 
        }

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@app.get(path="/indi")
async def load_indi(user_name: str, db: Session = Depends(get_db), user_data: dict = Depends(get_current)):
    try:
        # 오늘 업로드된 사진 불러오기
        photos = f_photo_crud.load_indi_photo(user_data.family_id, user_name, db)

        if not photos:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No photos found for today")

        return {
            "status": "success",
            "photos": [{photo.file, photo.photo_no} for photo in photos] 
        }

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    

@app.post("/comments")
async def create_comment(photo_no: str, comment: str, db: Session = Depends(get_db), user_data: dict = Depends(get_current)):
    new_comment = f_photo_crud.add_comment(photo_no, user_data.user_name, comment, db)
    return {
        "status": "success",
        "comment": {
            "comment_id": new_comment.comment_id,
            "user_name": new_comment.user_name,
            "comment": new_comment.comment,
            "regdate": new_comment.regdate
        }
    }

@app.get("/comments/{photo_no}")
async def get_comments(photo_no: str, db: Session = Depends(get_db)):
    comments = f_photo_crud.load_comments(photo_no, db)
    return {
        "status": "success",
        "comments": [
            {
                "comment_id": comment.comment_id,
                "user_name": comment.user_name,
                "comment": comment.comment,
                "regdate": comment.regdate
            } for comment in comments
        ]
    }