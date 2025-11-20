from pydantic import BaseModel, EmailStr


class UserResponse(BaseModel):
    username: str
    email: EmailStr

class UserSchema(UserResponse):
    password: str

class UserDb(UserSchema):
    id: int

