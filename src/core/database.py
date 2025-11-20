from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from config import settings

engine = create_engine(
    f"mysql+mysqlconnector://{settings.DB_USER}:{settings.DB_PWD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}",
    pool_pre_ping=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  
# SessionLocal serve para realizar transações ORM, diferente da engine que é apenas uma conexão que envia strings em formato de consulta para o banco 

def get_db():
    db = SessionLocal()
    try:
        yield db  # with automático, endpoint vai usar o objeto db e depois encerrar a sessão/conexão
    finally:
        db.close()
    