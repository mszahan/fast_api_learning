import contextlib
from fastapi import FastAPI, status, Depends, HTTPException

from sqlalchemy import exc, select
from sqlalchemy.ext.asyncio import AsyncSession

from database import create_all_tables, get_async_session
from models import User
from schemas import UserRead, UserCreate
from password import get_password_hash


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    await create_all_tables()
    yield


app = FastAPI(lifespan=lifespan)


@app.post('/register', status_code=status.HTTP_201_CREATED, response_model=UserRead)
async def register(user_create: UserCreate,
                   session: AsyncSession = Depends(get_async_session)) -> User:
    hashed_password = get_password_hash(user_create.password)
    user = User(
        **user_create.model_dump(exclude={'password'}), hashed_password=hashed_password)
    try:
        session.add(user)
        await session.commit()
    except exc.IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail='Email already exists'
        )
    return user
