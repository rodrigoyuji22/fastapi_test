from passlib.context import CryptContext

# instancia de cryptcontext com o algoritmo de hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# metodo para hashear a senha
def hash_password(password: str):
    return pwd_context.hash(password)


# metodo para verificar se a senha do dto é a mesma q a senha do db, vai aplicar hashing para verificar
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)
