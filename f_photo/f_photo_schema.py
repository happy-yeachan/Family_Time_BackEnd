from pydantic import BaseModel, EmailStr, validator

from fastapi import HTTPException


class Current_User(BaseModel):
    user_name: str
    family_id: str
