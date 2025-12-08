import asyncio
from fastapi import Depends, FastAPI
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import get_async_session
from core.handlers import register_exceptions_handlers
from schemas.user_schema import UserCreate, UserResponse, UserUpdate
from services.user_service import UserService

app = FastAPI()
register_exceptions_handlers(app)


@app.get("/", status_code=200)
async def Hello_World():
    await asyncio.sleep(10)
    return {"message": "Hello World"}


@app.post("/create/user", status_code=201, response_model=UserResponse)
async def create_user(user: UserCreate, session: AsyncSession = Depends(get_async_session)):
    service = UserService(session)
    return await service.create_user_service(user)


@app.get("/user/{user_id}", status_code=200, response_model=UserResponse)
async def get_user_by_id(
    user_id: int, session: AsyncSession = Depends(get_async_session)
):
    service = UserService(session)
    return await service.get_user_by_id_service(user_id)


@app.get(
    "/users", status_code=200, response_model=list[UserResponse]
)  # tava dando erro pois o reponse model deve ser uma lista de UserResponse, ao inves de UserReponse
async def get_users(session: AsyncSession = Depends(get_async_session)):
    service = UserService(session)
    return await service.get_users()


@app.delete("/delete/{user_id}", status_code=204)
async def delete_user(user_id: int, session: AsyncSession = Depends(get_async_session)):
    service = UserService(session)
    return await service.delete_user(user_id)


@app.patch("/update/{user_id}", status_code=204)
async def update_user(
    user_id: int, user: UserUpdate, session: AsyncSession = Depends(get_async_session)
):
    service = UserService(session)
    await service.update_user(user_id, user)
