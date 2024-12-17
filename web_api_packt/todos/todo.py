from fastapi import APIRouter, Path, HTTPException, status, Request, Depends
from fastapi.templating import Jinja2Templates
from model import Todo, TodoItem, TodoItems
from fastapi import Form

todo_router = APIRouter()

todo_list = []

templates = Jinja2Templates(directory='templates/')


@todo_router.post('/todo') ## added manually the successfull status
# async def add_todo(request:Request, todo: Todo = Depends(Todo.as_form)):
async def add_todo(request:Request, item: str = Form(...)):
    # todo.id = len(todo_list) + 1
    todo = Todo(id=len(todo_list) + 1, item=item)
    todo_list.append(todo)
    # return {'message': 'Todo added successfully'}
    return templates.TemplateResponse('todo.html', {'request':request, 'todos': todo_list})

## added a response model that will give todo without id
@todo_router.get('/todo', response_model=TodoItems)
async def retrive_todo(request: Request):
    # return {'todos': todo_list}
    return templates.TemplateResponse('todo.html', {'request':request, 'todos': todo_list})


@todo_router.get('/todo/{todo_id}')
async def get_single_todo(request: Request, todo_id: int = 
                          Path(..., title='The ID for the todo to retrive.')):
    for todo in todo_list:
        ## since you used model in todo:Todo you can use .notation
        if todo.id == todo_id:
            # return {
            #     'todo': todo
            # }
            return templates.TemplateResponse('todo.html', {'request': request, 'todo': todo})
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='The todo does not exist',
    )


@todo_router.put('/todo/{todo_id}')
async def update_todo(todo_data: TodoItem,
                      todo_id: int = Path(..., title='The Id of the todo to be updated') ) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {'message': 'Todo updated successfully'}
    # return {'message': 'Invalid Todo Id'}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='todo with the provided id does not exist'
    )


@todo_router.delete('/todo/{todo_id}')
async def delete_single_todo(todo_id: int) -> dict:
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)
            return {'message': 'Todo deleted successfully'}
    # return {'message': 'invalid todo id'}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Todo with supplied id does not exist'
    )


@todo_router.delete('/todo')
async def delete_all_todo() -> dict:
    todo_list.clear()
    return {'message': 'All todos deleted successfully'}