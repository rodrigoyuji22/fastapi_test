import asyncio
from fastapi import FastAPI
from core.handlers import register_exceptions_handlers
from routers import users, auth
#

app = FastAPI()
register_exceptions_handlers(app)
app.include_router(users.router)
app.include_router(auth.router)

@app.get("/", status_code=200)
async def Hello_World():
    await asyncio.sleep(10)
    return {"message": "Hello World"}
    
