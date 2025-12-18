from typing import Annotated

from fastapi import Depends
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordBearer
from jwt import ExpiredSignatureError, InvalidTokenError
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import async_session
from core.security import decode_access_token


async def get_async_session():
    async with async_session() as session:
        yield session


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def auth_user_retrieve_id(token: str = Depends(oauth2_scheme)) -> int:
    try:
        payload = decode_access_token(token=token)
        if "sub" not in payload:
            raise HTTPException(401, "Invalid token: missing object")
        return int(payload["sub"])
    except ExpiredSignatureError:
        raise HTTPException(401, "Token expired")
    except InvalidTokenError:
        raise HTTPException(401, "Invalid token")


session_dep = Annotated[AsyncSession, Depends(get_async_session)]
token_dep = Annotated[int, Depends(auth_user_retrieve_id)]
