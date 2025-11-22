import datetime
from typing import Optional
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
    username: Optional[str] = None
    email: Optional[EmailStr] = None


# Schemas não devem conter regra de negócio, são apenas dtos para validação dos dados do payload
# autenticação, regras de negócio e lógica devem ficar em services e nos endpoints