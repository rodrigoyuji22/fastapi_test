from fastapi import HTTPException
from sqlalchemy import select, update
from app import get_users
from models.user_model import User
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError


class UserRepository():
    def __init__(self, session: Session):
        self.db = session

    def add_user(self, user: User) -> User:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def get_user(self, user_id: int) -> User:
        return self.db.get(User, user_id)

    def get_users(self) -> list[User]:
        stmt = select(User)
        return self.db.scalars(stmt).all()
    
    def delete_user(self, user: User):
        self.db.delete(user)
        self.db.commit()

    def update_user(self, user: User) -> User:
        self.db.commit()
        self.db.refresh(user)
        return user
