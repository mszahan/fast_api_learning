from datetime import datetime
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel


fakedb = {}


class Item(BaseModel):
    title: str
    timestamp: datetime
    description: str | None = None


app = FastAPI()

@app.put('/items/{id}')
def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    fakedb[id] = json_compatible_item_data