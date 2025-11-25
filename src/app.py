from fastapi import Depends, FastAPI
from fastapi.responses import HTMLResponse
from core.database import get_session
from schemas.user_schema import UserCreate, UserResponse
from services.user_service import UserService
from sqlalchemy.orm import Session

app = FastAPI()

@app.get('/', status_code=200)
def Hello_World():
    return {'message': 'Hello World!'}

@app.post('/create/user', status_code=201, response_model=UserResponse)
def create_user(user: UserCreate, session: Session=Depends(get_session)): 
    service = UserService(session)
    created_user = service.create_user_service(user)
    return created_user

@app.get('/user/{id}', status_code=200, response_model=UserResponse)
def get_user_by_id(id: int, session: Session=Depends(get_session)):
    service = UserService(session)
    return service.get_user_by_id_service(id)

@app.get('/users', status_code=200, response_model=UserResponse)
def get_users():
    pass