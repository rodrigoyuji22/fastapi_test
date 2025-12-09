from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from passlib.context import CryptContext
from config import settings
from jwt import encode

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

def create_access_token(claims: dict):
    expire = datetime.now(tz=ZoneInfo('UTC')) + timedelta(minutes=settings.TOKEN_EXPIRE_MINUTES)
    payload = claims.copy()
    payload.update(
        {
            'iat': int(datetime.now(tz=ZoneInfo('UTC')).timestamp()),
            'exp': int(expire.timestamp()),
        }
    )
    token = encode(payload, settings.SECRET_KEY, algorithm=settings.TOKEN_ENCRYPT_ALGORITHM)
    return token