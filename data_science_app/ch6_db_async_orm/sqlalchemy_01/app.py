import contextlib
from fastapi import FastAPI
from sqlalchemy_01.database import get_async_session, create_all_tables


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    await create_all_tables()
    yield

app = FastAPI(lifespan=lifespan)
