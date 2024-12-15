from fastapi import APIRouter, Path
from model import Todo

todo_router = APIRouter()

todo_list = []

@todo_router.post('/todo')
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {'message': 'Todo added successfully'}

@todo_router.get('/todo')
async def retrive_todo() -> dict:
    return {'todos': todo_list}

@todo_router.get('/todo/{todo_id}')
async def get_single_todo(todo_id: int = 
                          Path(..., title='The ID for the todo to retrive.')) -> dict:
    for todo in todo_list:
        ## since you used model in todo:Todo you can use .notation
        if todo.id == todo_id:
            return {
                'todo': todo
            }
    return {
        'message': 'The todo id does not exists'
    }