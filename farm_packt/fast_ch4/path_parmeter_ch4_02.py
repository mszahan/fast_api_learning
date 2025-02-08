from fastapi import FastAPI


app = FastAPI()


@app.get('/car/{id}')
async def root(id):
    return {'cardid': id}

@app.get('/carh/{id}')
async def hited_car(id: int):
    return {'car_id': id}