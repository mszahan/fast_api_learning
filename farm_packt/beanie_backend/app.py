from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi_cors import CORS
from database import init_db
from routers.cars import router as cars_router
from routers.users import router as users_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(lifespan=lifespan)
CORS(app)

app.include_router(cars_router, prefix='/cars', tags=['Cars'])
app.include_router(users_router, prefix='/users', tags=['Users'])


@app.get('/', tags=['Root'])
async def read_root():
    return {"message": "Welcome to the Car Ads API"}
