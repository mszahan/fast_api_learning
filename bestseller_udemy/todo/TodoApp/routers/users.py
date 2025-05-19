from fastapi import APIRouter, Depends, HTTPException, Path
from starlette import status
from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from models import User
from database import SessionLocal
from .auth import get_current_user


router = APIRouter(
    prefix='/user',
    tags=['users']
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
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')



class UserVerification(BaseModel):
    password: str
    new_password: str = Field(min_length=6)



@router.get('/', status_code=status.HTTP_200_OK)
async def get_user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication failed')
    return db.query(User).filter(User.id == user.get('id')).first()


@router.put('/password', status_code=status.HTTP_204_NO_CONTENT)
async def change_password(user: user_dependency, db: db_dependency, 
                          user_verification: UserVerification):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication failed')
    user_model = db.query(User).filter(User.id == user.get('id')).first()
    if not bcrypt_context.verify(user_verification.password, user_model.hashed_password):
        raise HTTPException(status_code=401, detail='Error on password change')
    user_model.hashed_password = bcrypt_context.hash(user_verification.new_password)
    db.add(user_model)
    db.commit()




@router.put('/phone/{phone_number}', status_code=status.HTTP_200_OK)
async def update_phone_number(user: user_dependency, db: db_dependency, phone_number:str):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication failed')
    user = db.query(User).filter(User.id == user.get('id')).first()
    user.phone_number = phone_number
    db.add(user)
    db.commit()











