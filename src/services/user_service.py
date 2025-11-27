from sqlalchemy.orm import Session
from core.security import hash_password
from models.user_model import User
from repository.user_repository import UserRepository
from schemas.user_schema import UserCreate, UserUpdate
from core.exceptions import PasswordValidationError, UserNotFoundError


class UserService():
    def __init__(self, session: Session):
        self.repo = UserRepository(session)

    def create_user_service(self, userDto: UserCreate):
        if userDto.password != userDto.confirm_password:
            raise PasswordValidationError("Usuário não pode ser criado")
        hashed_password = hash_password(userDto.password)
        user = User(
            username = userDto.username,
            email = userDto.email,
            password = hashed_password
            )
        return self.repo.add_user(user)

    def get_user_by_id_service(self, dtoId: int):
        user = self.repo.get_user(dtoId)
        if user:
            return user
        raise UserNotFoundError("Usuário não encontrado")

    def get_users(self):
        return self.repo.get_users()

    def delete_user(self, dtoId: int):
        user = self.repo.get_user(dtoId)
        if not user:
            raise UserNotFoundError("Usuário não encontrado")  # noqa: F821
        self.repo.delete_user(user)

    def update_user(self, dtoId: int, userDto: UserUpdate):
        user = self.repo.get_user(dtoId)
        if not user:
            raise UserNotFoundError("Usuário não encontrado")
        if userDto.username is not None:
            user.username = userDto.username
        if userDto.email is not None:
            user.email = userDto.email
        return self.repo.update_user(user)
