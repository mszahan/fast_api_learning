from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.users import register as users_router


origins = ['*']

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)