from typing import Annotated
from fastapi import FastAPI, Header


app = FastAPI()


@app.get('/headers')
async def read_header(user_agent: Annotated[str | None, Header()] =None):
    return {'User-agent': user_agent}

