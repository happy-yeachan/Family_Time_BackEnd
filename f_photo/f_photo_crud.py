from sqlalchemy.orm import Session
from models import Family_Photo
import base64
from fastapi import UploadFile
from datetime import datetime
from sqlalchemy import func
# def get_family(id: str, db: Session):  
#     return db.query(Family).filter(Family.id == id).first()


def upload_photo(file: UploadFile, comment: str, user_name: str, family_id: str, db: Session):
    # 파일 내용을 읽어서 Base64로 인코딩
    file_content = file.file.read()
    encoded_file = base64.b64encode(file_content).decode('utf-8')  # Base64로 인코딩하고 문자열로 변환

    # Family_Photo 모델 인스턴스 생성
    family_photo = Family_Photo(
        author = user_name,
        comment = comment,
        family_id = family_id,
        file = encoded_file  # Base64 인코딩된 파일 데이터를 저장
    )

    # 데이터베이스에 저장
    db.add(family_photo)
    db.commit()
    db.refresh(family_photo)  # 새로 추가된 엔티티를 새로 고침하여 최신 상태로 가져옴

    return family_photo  # 저장된 사진 정보 반환


def load_today_photo(family_id: str, db: Session):
    # 오늘 날짜 구하기
    today = datetime.now().date()

    # 오늘 업로드된 사진 쿼리
    photos = db.query(Family_Photo).filter(
        Family_Photo.family_id == family_id,
        func.date(Family_Photo.regdate) == today  # 오늘 날짜와 일치하는 사진 필터링
    ).all()

    return photos  # 오늘 업로드된 사진 리스트 반환

def load_all_photo(family_id: str, db: Session):

    # 오늘 업로드된 사진 쿼리
    photos = db.query(Family_Photo).filter(
        Family_Photo.family_id == family_id # 오늘 날짜와 일치하는 사진 필터링
    ).all()

    return photos  # 오늘 업로드된 사진 리스트 반환

def load_indi_photo(family_id: str, user_name: str, db: Session):
    # 오늘 업로드된 사진 쿼리
    photos = db.query(Family_Photo).filter(
        Family_Photo.family_id == family_id,
        func.date(Family_Photo.username) == user_name  # 오늘 날짜와 일치하는 사진 필터링
    ).all()

    return photos