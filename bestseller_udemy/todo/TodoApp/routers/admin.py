from fastapi import APIRouter, Depends, HTTPException, Path
from starlette import status
from typing import Annotated
from sqlalchemy.orm import Session
from models import Todo
from database import SessionLocal
from .auth import get_current_user


router = APIRouter(
    prefix='/admin',
    tags=['admin']
)


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
user_dependency = Annotated[dict, Depends(get_current_user)]


@router.get('/todo', status_code=status.HTTP_200_OK)
async def all_todo_list(user: user_dependency, db: db_dependency):
    if user is None or user.get('user_role') != 'admin':
        raise HTTPException(status_code=401, detail='Authentication failed')
    return db.query(Todo).all()


@router.delete('/todo/{todo_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(user: user_dependency, db: db_dependency, todo_id: int = Path(gt=0)):
    if user is None or user.get('user_role') != 'admin':
        raise HTTPException(status_code=401, detail='authentication failed')
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail='No todo found')
    db.delete(todo)
    db.commit()