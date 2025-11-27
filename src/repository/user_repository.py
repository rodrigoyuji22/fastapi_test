from typing import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

from models.user_model import User


class UserRepository:
    def __init__(self, session: Session):
        self.db = session

    def add_user(self, user: User) -> User:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_user(self, user_id: int) -> User:
        return self.db.get(User, user_id)  # pyright: ignore[reportReturnType]

    def get_users(self) -> Sequence[User]:  # noqa: F811
        stmt = select(User)
        return self.db.scalars(stmt).all()

    def delete_user(self, user: User):
        self.db.delete(user)
        self.db.commit()

    def update_user(self, user: User) -> User:
        self.db.commit()
        self.db.refresh(user)
        return user
