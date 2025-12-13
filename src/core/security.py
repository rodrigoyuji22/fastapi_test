from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import jwt
from jwt import ExpiredSignatureError, InvalidTokenError, encode
from passlib.context import CryptContext
from core.config import settings

# instancia de cryptcontext com o algoritmo de hashing
pwd_context = CryptContext(
    schemes=[settings.CRYPT_SCHEME],
    deprecated=settings.CRYPT_DEPRECATED,
)


# metodo para hashear a senha
def hash_password(password: str):
    return pwd_context.hash(password)


# metodo para verificar se a senha do dto é a mesma q a senha do db, vai aplicar hashing para verificar
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(claims: dict) -> str:
    expires = datetime.now(tz=ZoneInfo("UTC")) + timedelta(
        minutes=settings.TOKEN_EXPIRE_MINUTES
    )
    payload = claims.copy()
    payload.update(
        {
            "iat": int(datetime.now(tz=ZoneInfo("UTC")).timestamp()),
            "exp": int(expires.timestamp()),
        }
    )
    token = encode(
        payload, settings.SECRET_KEY, algorithm=settings.TOKEN_ENCRYPT_ALGORITHM
    )
    return token


def decode_access_token(token: str) -> dict:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.TOKEN_ENCRYPT_ALGORITHM]
        )
        return payload
    except ExpiredSignatureError:
        raise ExpiredSignatureError("Token expired")
    except InvalidTokenError:
        raise InvalidTokenError("Invalid token")
