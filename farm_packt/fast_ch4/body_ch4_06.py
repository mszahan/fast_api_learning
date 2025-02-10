from typing import Dict
from fastapi import FastAPI, Body


app = FastAPI()


@app.post('/cars')
async def new_car(data: Dict = Body(...)):
    print(data)
    return{'Cars': data}
