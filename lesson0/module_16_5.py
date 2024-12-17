from fastapi import FastAPI, Request, Path, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Annotated, List
import uvicorn

# Задача "Список пользователей в шаблоне"

app = FastAPI(swagger_ui_parameters={'tryItOutEnabled': True}, debug=True)

# Настраиваем Jinja2 для загрузки шаблонов из папки templates
templates = Jinja2Templates(directory='templates')

class User(BaseModel):
    id: int = None  # ID номер пользователя
    username: str = ''  # Имя пользователя
    age: int = None  # Возраст пользователя


users: List[User] = []


# Список пользователей (GET)
@app.get('/', response_class=HTMLResponse)
async def get_main_page(request: Request):
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})


# Получение пользователя по ID (GET)
@app.get('/user/{user_id}', response_class=HTMLResponse)
async def get_user(request: Request, user_id: Annotated[int, Path(ge=1)]):
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse('users.html', {'request': request, 'user': user})
    raise HTTPException(status_code=404, detail='User not found')


# Создание нового пользователя (POST)
@app.post('/user/{username}/{age}', response_class=HTMLResponse)
async def create_user(
    request: Request,
    username: Annotated[str, Path(min_length=3, max_length=100)],
    age: Annotated[int, Path(ge=1)]
    ):
    new_id = max(user.id for user in users) + 1 if users else 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})


# Обновление пользователя (PUT)
@app.put('/user/{user_id}/{username}/{age}', response_class=HTMLResponse)
async def update_user(
    request: Request,
    user_id: Annotated[int, Path(ge=1)],
    username: Annotated[str, Path(min_length=3, max_length=100)],
    age: Annotated[int, Path(ge=1)]
):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return templates.TemplateResponse('users.html', {'request': request, 'users': users})
    raise HTTPException(status_code=404, detail='User not found')


# Удаление пользователя (DELETE)
@app.delete('/user/{user_id}', response_class=HTMLResponse)
async def delete_user(request: Request, user_id: Annotated[int, Path(ge=1)]):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return templates.TemplateResponse('users.html', {'request': request, 'users': users})
    raise HTTPException(status_code=404, detail='User not found')


if __name__ == '__main__':
    uvicorn.run(app)
