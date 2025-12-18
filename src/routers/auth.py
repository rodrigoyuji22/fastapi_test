from fastapi.routing import APIRouter

from core.deps import session_dep
from schemas.token_schema import Token
from schemas.user_schema import UserAuthenticate
from services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", status_code=201, response_model=Token)
async def authenticate_user(userDto: UserAuthenticate, session: session_dep):
    service = AuthService(session)
    return await service.authenticate_user(userDto.email, userDto.password)
