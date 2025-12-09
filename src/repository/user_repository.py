from typing import Sequence
from sqlalchemy import select, or_
from sqlalchemy.ext.asyncio import AsyncSession
from models.user_model import User


class UserRepository:
    def __init__(self, session: AsyncSession):
        self.db = session

    async def validate_username_email(self, username: str, email: str):
        stmt = select(User).where(or_(
            User.username == username,
            User.email == email
        ))
        return await self.db.scalar(stmt)
        
    async def get_user_id(self, username: str):
        stmt = select(User.id).where(User.username == username)
        return await self.db.scalar(stmt)
        
    async def add_user(self, user: User) -> User:
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def get_user(self, user_id: int) -> User | None:
        return await self.db.get(User, user_id)

    async def get_users(self) -> Sequence[User]:
        stmt = select(User)
        result = await self.db.scalars(stmt)
        return result.all()
    # result é um objeto do tipo ScalarResult e .all é um método dessa classe

    async def delete_user(self, user: User):
        self.db.delete(user) # pyright: ignore
        await self.db.commit()

    async def update_user(self, user: User) -> User:
        await self.db.commit()
        await self.db.refresh(user)
        return user
