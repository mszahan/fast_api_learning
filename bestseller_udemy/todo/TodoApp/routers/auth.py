from fastapi import APIRouter, Depends, HTTPException, Path
from starlette import status
from typing import Annotated
from pydantic import BaseModel
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from models import User
from database import SessionLocal


router = APIRouter()

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


class UserRequest(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str
    password: str
    role: str


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



@router.post('/auth', status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, user_request: UserRequest):
    user = User(
        email=user_request.email,
        username=user_request.username,
        first_name=user_request.first_name,
        last_name=user_request.last_name,
        role=user_request.role,
        # hasing the password the passing it to the database stage
        hashed_password=bcrypt_context.hash(user_request.password),
        is_active=True

    )
    db.add(user)
    db.commit()