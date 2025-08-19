from enum import Enum
from fastapi import FastAPI, Query


class UsersFormat(str, Enum):
    SHORT = 'short'
    FULL = 'full'


app = FastAPI()


@app.get('/users')
async def get_user(format: UsersFormat):
    return {'format': format}
