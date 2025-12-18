from fastapi import APIRouter

from core.deps import session_dep, token_dep
from schemas.user_schema import UserCreate, UserResponse, UserUpdate
from services.user_service import UserService

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/create", status_code=201, response_model=UserResponse)
async def create_user(
    user: UserCreate, session: session_dep
):
    service = UserService(session)
    return await service.create_user_service(user)


@router.get("/list", status_code=200, response_model=list[UserResponse])
async def get_users(session: session_dep):
    service = UserService(session)
    return await service.get_users()


@router.get("/{user_id}", status_code=200, response_model=UserResponse)
async def get_user_by_id(
    user_id: int, session: session_dep
):
    service = UserService(session)
    return await service.get_user_by_id_service(user_id)


@router.delete("/delete/{user_id}", status_code=204)
async def delete_user(user_id: int, session: session_dep):
    service = UserService(session)
    return await service.delete_user(user_id)


@router.patch("/update", status_code=204)
async def update_user(
    user: UserUpdate, id: token_dep, session: session_dep):
    service = UserService(session)
    await service.update_user(id, user)
