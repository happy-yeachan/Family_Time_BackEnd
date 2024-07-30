from pydantic import BaseModel, EmailStr, validator


class NewFamilyForm(BaseModel):
    name: str
    id: str
  
