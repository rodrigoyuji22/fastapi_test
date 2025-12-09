from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models.user_model import User

class AuthRepository:
    
    def __init__(self, session: AsyncSession):
        self.db = session
    
    async def get_user_auth(self, email: str):
        stmt = select(User).where(
            User.email == email
        )
        return await self.db.scalar(stmt) 
        
        
    