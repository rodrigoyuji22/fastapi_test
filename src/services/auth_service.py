from sqlalchemy.ext.asyncio.session import AsyncSession

from core.exceptions import InvalidCredentialsError
from core.security import create_access_token, verify_password
from repository.auth_repository import AuthRepository


class AuthService:
    def __init__(self, session: AsyncSession):
        self.repo1 = AuthRepository(session)

    async def authenticate_user(self, email: str, password: str):
        result = await self.repo1.get_user_auth(email)
        if result is None:
            raise InvalidCredentialsError("Invalid credentials")
        pwd = result.password
        if not verify_password(password, pwd):
            raise InvalidCredentialsError("Invalid credentials")
        user_id = result.id
        if not user_id:
            raise InvalidCredentialsError("Sorry! Invalid credentials")
        claims = {"sub": user_id}
        return create_access_token(claims)
