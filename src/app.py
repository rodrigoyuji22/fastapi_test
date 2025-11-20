from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from schemas.user_schema import UserSchema, UserResponse

app = FastAPI()

@app.get('/', status_code=200)
def Hello_World():
    return {'message': 'Hello World!'}

@app.get('/hello', response_class=HTMLResponse)
def hello_html():
    return"""
    <html>
      <head>
        <title> Nosso olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo </h1>
      </body>
    </html>"""

@app.post('/create/user', status_code=201, response_model=UserResponse)
def create_user(user: UserSchema):  # recebe como parâmetro um user que é do tipo UserSchema
    return user

# se o cliente não enviar um user com so tipos especificados no schema, vai retornar 422