from fastapi import HTTPException
from models.user_model import User
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError


class UserRepository():
    def __init__(self, session: Session):
        self.db = session

    def add_user(self, user: User):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def get_user(self, user_id: int):
        return self.db.get(User, user_id)
