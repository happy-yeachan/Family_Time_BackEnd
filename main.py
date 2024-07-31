from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import models
from database import engine
models.Base.metadata.create_all(bind=engine)

from user import user_router
from family import family_router
from f_photo import f_photo_router
from CLOVA_Chatbot import log_router
origins = [
    "*"
]


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,  # cross-origin request에서 cookie를 포함할 것인지 (default=False)
    allow_methods=["*"],     # cross-origin request에서 허용할 method들을 나타냄. (default=['GET']
    allow_headers=["*"],     # cross-origin request에서 허용할 HTTP Header 목록
)
app.include_router(user_router.app, tags=["user"])
app.include_router(family_router.app, tags=["family"])
app.include_router(f_photo_router.app, tags=["f_photo"])
app.include_router(log_router.app, tags=["chatbot"])



@app.get("/")
def read_root():
    return {"Hello": "World"}