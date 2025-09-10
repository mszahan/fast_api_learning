from typing import Annotated

from fastapi import Cookie, FastAPI
from pydantic import BaseModel


app = FastAPI()


class Cookies(BaseModel):
    # you can also extra cookies
    model_config = {'extra': 'forbid'}

    session_id: str
    facebook_tracker: str | None = None
    google_tracker: str | None = None


@app.get('/items')
async def read_items(cookies: Annotated[Cookies, Cookie()]):
    return cookies
