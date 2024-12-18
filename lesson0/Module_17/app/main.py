from fastapi import FastAPI
from routers import task, user
import uvicorn

app = FastAPI()
app.include_router(task.task_router)
app.include_router(user.user_router)


@app.get('/')
async def welcome():
    return {'message': 'Welcome to Taskmanager'}


if __name__ == '__main__':
    uvicorn.run(app)
