from datetime import datetime
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str
    confirm_password: str

class UserResponse(UserBase):
    id: int
    created_at: datetime

class UserUpdate(BaseModel):
    username: str | None
    email: str | None

class UserAuthenticate(BaseModel):
    email: EmailStr
    password: str


# Schemas são dtos para validação dos dados do payload