from typing import Annotated
from pydantic import BaseModel, EmailStr
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db_connection import get_session
from models import User, Role
from operations import add_user
from security import decode_access_token, oauth2_scheme


class UserCreateRequestWithRole(BaseModel):
    username: str
    email: EmailStr
    role: Role


def get_current_user(
        token: Annotated[str, Depends(oauth2_scheme)],
        session: Session = Depends(get_session),) -> UserCreateRequestWithRole:
    user = decode_access_token(token, session)
    return UserCreateRequestWithRole(
        username=user.username,
        email=user.email,
        role=user.role,
    )


def get_premium_user(current_user: Annotated[get_current_user, Depends()]):
    if current_user.role != Role.premium:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='User not authorized')
    return current_user


router = APIRouter()


@router.get('/welcome/all-users')
def all_users_can_access(user: Annotated[get_current_user, Depends()]):
    return {'message': f'{user.username} authorized'}


@router.get('/welcome/premium-users', responses={
    status.HTTP_401_UNAUTHORIZED: {
        'description': 'User not authorized'
    }
})
def premium_users_can_access(user: Annotated[get_premium_user, Depends()]):
    return {'message': f'{user.username} authorized as premium user'}
