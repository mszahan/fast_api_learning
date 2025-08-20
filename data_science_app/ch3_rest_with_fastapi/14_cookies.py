from fastapi import FastAPI, Cookie


app = FastAPI()


async def get_cookie(hello: str | None = Cookie(None)):
    return {'hello': hello}
