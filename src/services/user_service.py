# aqui vai o service de crud 
from models.user_model import User
from schemas.user_schema import UserCreate


def create_user(userDto: UserCreate):
    if userDto.password == userDto.confirm_password:
        hashed_password = userDto.password
        user = User(
            username = userDto.username,
            email = userDto.email,
            password = hashed_password
        )
