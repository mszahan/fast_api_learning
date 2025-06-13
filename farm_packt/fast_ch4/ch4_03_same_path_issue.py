from fastapi import FastAPI

app = FastAPI()


#if it become the first route it will work
@app.get('/user/me')
async def me_user():
    return {'userid': 'this is me'}


@app.get('/user/{id}')
async def user(id:int):
    return {'userid': id}

