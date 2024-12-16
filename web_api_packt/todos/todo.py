from fastapi import APIRouter, Path, HTTPException, status
from model import Todo, TodoItem, TodoItems

todo_router = APIRouter()

todo_list = []

@todo_router.post('/todo', status_code=201) ## added manually the successfull status
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {'message': 'Todo added successfully'}

## added a response model that will give todo without id
@todo_router.get('/todo', response_model=TodoItems)
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