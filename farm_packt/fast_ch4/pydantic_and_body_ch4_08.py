from fastapi import FastAPI, Body
from pydantic import BaseModel


class InsertCar(BaseModel):
    brand: str
    model: str
    year: int

class UserModel(BaseModel):
    username: str
    name: str


app = FastAPI()


@app.post('/cars/user')
async def new_car_model(car: InsertCar, user: UserModel, code: int = Body(None)):
    return {'car': car, 'user': user, 'code': code}

## this is how you need to send request

# {
#     "car": {
#     "brand": "unknown",
#     "model":"Unknown",
#     "year":2014
#     },
#     "user": {
#     "username":"john",
#     "name": "john"
#     },
#     "code": 23

# }