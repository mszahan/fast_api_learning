from typing import Annotated
from fastapi import FastAPI, Path


app = FastAPI()


@app.get('/items/{item_id}')
async def read_items(
    item_id: Annotated[int, Path(gt=0, le=1000)],
    q: str
):
    results = {'item_id': item_id}
    return results
