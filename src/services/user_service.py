from sqlalchemy.ext.asyncio import AsyncSession
from core.exceptions import PasswordValidationError, UserNotFoundError
from core.security import hash_password
from models.user_model import User
from repository.user_repository import UserRepository
from schemas.user_schema import UserCreate, UserUpdate


class UserService:
    def __init__(self, session: AsyncSession):
        self.repo = UserRepository(session)

    async def create_user_service(self, userDto: UserCreate):
        if userDto.password != userDto.confirm_password:
            raise PasswordValidationError(
                "Usuário não pode ser criado, senhas incosistentes"
            )
        hashed_password = hash_password(userDto.password)
        user = User(
            username=userDto.username, email=userDto.email, password=hashed_password
        )
        return await self.repo.add_user(user)

    async def get_user_by_id_service(self, dtoId: int):
        user = await self.repo.get_user(dtoId)
        if user:
            return user
        raise UserNotFoundError("Usuário não encontrado")

    async def get_users(self):
        return await self.repo.get_users()

    async def delete_user(self, dtoId: int):
        user = await self.repo.get_user(dtoId)
        if not user:
            raise UserNotFoundError("Usuário não encontrado")  # noqa: F821
        await self.repo.delete_user(user)

    async def update_user(self, dtoId: int, userDto: UserUpdate):
        user = await self.repo.get_user(dtoId)
        if not user:
            raise UserNotFoundError("Usuário não encontrado")
        if userDto.username is not None:
            user.username = userDto.username
        if userDto.email is not None:
            user.email = userDto.email
        return await self.repo.update_user(user)
