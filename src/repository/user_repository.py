from models.user_model import User
from sqlalchemy.orm import Session


class UserRepository():
    def __init__(self, session: Session):
        self.db = session

    def add_user(self, user: User):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user