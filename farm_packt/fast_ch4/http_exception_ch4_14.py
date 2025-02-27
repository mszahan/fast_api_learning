from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, status


app = FastAPI()

class InsertCar(BaseModel):
    brand: str
    model: str
    year: int


@app.post('/carmodel')
async def new_car_model(car: InsertCar):
    if car.year > 2022:
        raise HTTPException(status.HTTP_406_NOT_ACCEPTABLE, detail= 'The car does not exist yet')
    return {'message': car}

