from core.security import hash_password, verify_password
from models.user_model import User
from repository.user_repository import UserRepository
from schemas.user_schema import UserCreate
from sqlalchemy.orm import Session


class UserService():
    def __init__(self, session: Session):
        self.repo = UserRepository(session)

    def _create_user(self, userDto: UserCreate):
        if userDto.password == userDto.confirm_password:
            hashed_password = hash_password(userDto.password)
            user = User(
                username = userDto.username,
                email = userDto.email,
                password = hashed_password
            )
        return self.repo.add_user(user)
