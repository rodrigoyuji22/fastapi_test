from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from core.deps import get_async_session
from schemas.token_schema import Token
from schemas.user_schema import UserAuthenticate
from services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", status_code=201, response_model=Token)
async def authenticate_user(userDto: UserAuthenticate, session: AsyncSession = Depends(get_async_session)):
    service = AuthService(session)
    return await service.authenticate_user(userDto.email, userDto.password)
