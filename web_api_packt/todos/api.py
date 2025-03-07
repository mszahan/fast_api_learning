from fastapi import FastAPI
from todo import todo_router

app = FastAPI()

@app.get('/')
async def welcome() -> dict:
    return {'message': 'Hello fastapi hola'}


## to enable the visibility of the Todo router to uvicorn

app.include_router(todo_router)