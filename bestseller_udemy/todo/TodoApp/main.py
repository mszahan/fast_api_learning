from fastapi import FastAPI, Depends
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

@app.get('/')
async def todo_list(db: db_dependency):
    return db.query(Todo).all()
