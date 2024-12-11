from fastapi import FastAPI, Path, status, Body, HTTPException
from pydantic import BaseModel
from typing import List

# Задача "Модель пользователя"

app = FastAPI()
users = []


class User(BaseModel):
    id: int = None  # ID номер пользователя
    username: str = ''  # Имя пользователя
    age: int = None  # Возраст пользователя


def get_last_id(users_list: list):
    last_id: int = 0
    for u in users_list:
        if last_id < u.id:
            last_id = u.id
    return last_id


def get_user(users_list: list, user_id: int):
    for u in users_list:
        if u.id == user_id:
            return u


# Получение всех элементов списка пользователей
@app.get('/users')
async def get_all_users() -> List[User]:
    return users


# Добавление одного нового пользователя в список
@app.post('/user/{username}/{age}')
async def create_user(
        username: str = Path(min_length=3, max_length=20, description='Enter username', example='UrbanUser'),
        age: int = Path(ge=18, le=120, description='Enter age', example=20)) -> User:
    new_user = User()
    new_user.id = get_last_id(users) + 1 if len(users) > 0 else 1
    new_user.username = username
    new_user.age = age
    users.append(new_user)
    return new_user


# Редактирование пользователя в списке по его ID
@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int = Path(ge=1, le=100, description='Enter user_id', example=10),
                      username: str = Path(min_length=3, max_length=20, description='Enter username',
                                           example='UrbanUser'),
                      age: int = Path(ge=18, le=120, description='Enter age', example=20)) -> User:
    try:
        edit_user = get_user(users, user_id)
        edit_user.username = username
        edit_user.age = age
        return edit_user
    except:
        raise HTTPException(status_code=404, detail='User was not found')


# Удаление пользователя из списка по его ID
@app.delete('/user/{user_id}')
async def delete_user(user_id: int = Path(ge=1, le=100, description='Enter user_id', example=10)) -> User:
    try:
        del_user = users.pop(users.index(get_user(users, user_id)))
        return del_user
    except:
        raise HTTPException(status_code=404, detail='User was not found')
