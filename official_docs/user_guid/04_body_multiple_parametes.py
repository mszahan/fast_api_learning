from typing import Annotated
from fastapi import FastAPI, Path, Body
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None

# Mix Path, Query and body parameters------------


@app.put('/mix/{item_id}')
async def mix(
    item_id: Annotated[int, Path(ge=0, le=1000)],
    q: str | None = None,
    # made the body optional
    item: Item | None = None
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results

# Multiple body parameters------------
# it will expect the folloing body
# {
#     "item": {
#         "name": "Foo",
#         "description": "The pretender",
#         "price": 42.0,
#         "tax": 3.2
#     },
#     "user": {
#         "username": "dave",
#         "full_name": "Dave Grohl"
#     }
# }


@app.put('/multiple/{item_id}')
async def multiple_body(
    item_id: int, item: Item, user: User
):
    results = {"item_id": item_id, "item": item, "user": user}
    return results


# Singular values in body--------------------
# when you have single input as body just use Body without andy pydantic model


@app.put('/single/{item_id}')
async def single_body(
    item_id: int, item: Item, user: User, importance: Annotated[int, Body()]
):
    results = {"item_id": item_id, "item": item,
               "user": user, "importance": importance}
    return results


# Embed a single body parameter¶------------------------------------
# when you want the single model to be embed like the follwoing
# 'item':--
# {
#     "item": {
#         "name": "Foo",
#         "description": "The pretender",
#         "price": 42.0,
#         "tax": 3.2
#     }
# }

@app.put('/embed/{item_id}')
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results
