from fastapi import FastAPI, Depends, HTTPException, Path
from starlette import status
from typing import Annotated
from sqlalchemy.orm import Session
from . import models
from .models import Todo
from .database import engine, SessionLocal


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get('/', status_code=status.HTTP_200_OK)
async def todo_list(db: db_dependency):
    return db.query(Todo).all()


@app.get('/todo/{todo_id}')
async def todo_detail(db: db_dependency, todo_id: int = Path(gt=0)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first() # first stops further filtering when the first id is found
    if todo is not None:
        return todo
    raise HTTPException(status_code=404, detail='Todo not found')