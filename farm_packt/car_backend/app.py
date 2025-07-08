from fastapi import FastAPI
from motor import motor_asyncio
from config import BaseConfig
from routers.cars import router as cars_router

settings = BaseConfig()


async def lifespan(app: FastAPI):
    app.client = motor_asyncio.AsyncIOMotorClient(settings.DB_URL)
    app.db = app.client[settings.DB_NAME]
    try:
        app.client.admin.command('ping')
        print('Pinged your deployment, you have successfully connected to mongodb')
        print('Mongodb address:', settings.DB_URL)
    except Exception as e:
        print(e)
    yield
    app.client.close()


app = FastAPI(lifespan=lifespan)
app.include_router(cars_router, prefix='/cars', tags=['cars'])


@app.get('/')
async def get_root():
    return ({'Message': 'Hello root'})
