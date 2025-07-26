from fastapi import FastAPI, HTTPException, status
from models import Task, TaskWithID, UpdateTask
from operations import read_all_tasks, read_task, create_task, modify_task, remove_task


app = FastAPI()


@app.get('/tasks', response_model=list[TaskWithID])
def get_tasks():
    tasks = read_all_tasks()
    return tasks


@app.get('/task/{task_id}')
def get_task(task_id: int):
    task = read_task(task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Task not found')
    return task


@app.post('/task', response_model=TaskWithID)
def add_task(task: Task):
    return create_task(task)


@app.put('/task/{task_id}', response_model=TaskWithID)
def update_task(task_id: int, task_update: UpdateTask):
    modified = modify_task(task_id, task_update.model_dump(exclude_unset=True))
    if not modified:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Task not found')
    return modified


@app.delete("/task/{task_id}", response_model=Task)
def delete_task(task_id: int):
    removed_task = remove_task(task_id)
    if not removed_task:
        raise HTTPException(
            status_code=404, detail="task not found"
        )
    return removed_task
