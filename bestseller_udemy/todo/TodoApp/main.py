from fastapi import FastAPI, Depends, HTTPException, Path
from starlette import status
from pydantic import BaseModel, Field
from typing import Annotated
from sqlalchemy.orm import Session
from . import models
from .models import Todo
from .database import engine, SessionLocal


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# it create connection with dabase and when request is done it closes the connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# it's simmilar to db: Session = Depends(get_db)
# which return database in db variable
db_dependency = Annotated[Session, Depends(get_db)]


class TodoRequest(BaseModel):
    title: str = Field(min_length=5)
    description: str = Field(min_length=5, max_length=100)
    priority: int = Field(gt=0, lt=6)
    complete: bool




@app.get('/', status_code=status.HTTP_200_OK)
async def todo_list(db: db_dependency):
    return db.query(Todo).all()


@app.get('/todo/{todo_id}', status_code=status.HTTP_200_OK)
async def todo_detail(db: db_dependency, todo_id: int = Path(gt=0)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first() # first stops further filtering when the first id is found
    if todo is not None:
        return todo
    raise HTTPException(status_code=404, detail='Todo not found')


@app.post('/todo', status_code=status.HTTP_201_CREATED)
async def create_todo(db:db_dependency, todo_request: TodoRequest):
    todo = Todo(**todo_request.model_dump())
    db.add(todo) # this line stages doesn't save on database
    db.commit() # this line makes the commit and save data on database
