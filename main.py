from typing import Union
from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def home():
    return {'Hello': 'World'}

@app.get("/items/{item_id}")
def item(item_id:int, q:Union[str, None] = None):
    return {"Item Id": item_id, "query":q}
