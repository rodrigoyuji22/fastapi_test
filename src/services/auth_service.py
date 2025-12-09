from sqlalchemy.ext.asyncio.session import AsyncSession
from core.security import verify_password, create_access_token
from src.repository.auth_repository import AuthRepository
from core.exceptions import InvalidCredentialsError
from src.repository.user_repository import UserRepository


class UserService:
    def __init__(self, session: AsyncSession):
        self.repo1 = AuthRepository(session)
        self.repo2 = UserRepository(session)
        
    async def authenticate_user(self, email: str, password: str):
        result = await self.repo1.get_hash_pwd(email)
        if result is None:
            raise InvalidCredentialsError("Invalid credentials")
        pwd = result.password
        if not verify_password(password, pwd):
            raise InvalidCredentialsError("Invalid credentials")
        user_id = await self.repo2.get_user_id(result.username)
        if not user_id:
            raise InvalidCredentialsError("Sorry! Invalid credentials")
        claims = {
            'sub': user_id
        }
        return create_access_token(claims)
        
                