from fastapi import FastAPI, Path
from typing import Annotated

# Задача "Имитация работы с БД"

app = FastAPI()
messages_db = {'0': 'First post in FastAPI'}
users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def get_all_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def new_user(username: str = Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser'),
                   age: int = Path(ge=18, le=120, description='Enter age', example=24)) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} is registered'


@app.put('/user/{user_id}/{username}/{age}')
async def upd_user(user_id: str = Path(ge=1, le=100, description='Enter user_id', example=24),
                   username: str = Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser'),
                   age: int = Path(ge=18, le=120, description='Enter age', example=24)) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} is updated'


@app.delete('/user/{user_id}')
async def del_user(user_id: str = Path(ge=1, le=100, description='Enter user_id', example=24)) -> str:
    users.pop(user_id)
    return f'User {user_id} is deleted'
