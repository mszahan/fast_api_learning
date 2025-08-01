from typing import Optional
from fastapi import FastAPI, HTTPException, status
from models import Task, TaskWithID, UpdateTask, TaskV2WithID
from operations import (read_all_tasks, read_task, create_task,
                        modify_task, remove_task, read_all_tasks_v2)


app = FastAPI(
    title='Task Manager API',
    description='This is a task management API',
    version='0.1.0'
)


@app.get('/tasks', response_model=list[TaskWithID])
def get_tasks(status: Optional[str] = None, title: Optional[str] = None):
    tasks = read_all_tasks()
    if status:
        tasks = [task for task in tasks if task.status == status]
    if title:
        tasks = [task for task in tasks if task.title == title]
    return tasks


@app.get('/v2/tasks', response_model=list[TaskV2WithID])
def get_tasks_v2():
    tasks = read_all_tasks_v2()
    return tasks


@app.get('/task/search', response_model=list[TaskWithID])
def search_tasks(keyword: str):
    tasks = read_all_tasks()
    filtered_tasks = [task for task in tasks if keyword.lower() in (
        task.title + task.description).lower()]
    return filtered_tasks


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
