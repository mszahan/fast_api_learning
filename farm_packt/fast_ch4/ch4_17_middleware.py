from fastapi import FastAPI, Request
from random import randint


app = FastAPI()

@app.middleware('http')
async def add_random_header(request: Request, call_next):
    number = randint(1, 100)
    response = await call_next(request)
    response.headers['X-Random'] = str(number)
    return response


@app.get('/')
async def read_root():
    return {'Hello': 'World'}
