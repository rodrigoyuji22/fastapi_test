from core.security import hash_password, verify_password
from models.user_model import User
from repository.user_repository import UserRepository
from schemas.user_schema import UserCreate
from sqlalchemy.orm import Session
from fastapi import HTTPException



class UserService():
    def __init__(self, session: Session):
        self.repo = UserRepository(session)

    def create_user_service(self, userDto: UserCreate):
        if userDto.password != userDto.confirm_password:
            raise HTTPException(400, "Usuário não pode ser criado")
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
        raise HTTPException(404, 'Usuário não encontrado')
    
    def get_users(self):
        return self.repo.get_users()
