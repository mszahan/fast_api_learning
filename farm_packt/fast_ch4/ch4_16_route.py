from fastapi import FastAPI
from routers.users import router as users_router
from routers.cars import router as cars_router


app = FastAPI()


app.include_router(users_router, prefix='/users', tags=['users'])
app.include_router(cars_router, prefix='/cars', tags=['cars'])
