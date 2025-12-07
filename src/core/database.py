from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from core.config import settings

engine = create_async_engine(
    f"mysql+asyncmy://{settings.DB_USER}:{settings.DB_PWD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}",
    pool_pre_ping=True,
)

async_session = async_sessionmaker(expire_on_commit=False, autocommit=False, autoflush=False, bind=engine)


async def get_async_session():
    async with async_session() as session:
        yield session
