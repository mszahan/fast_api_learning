from fastapi import FastAPI, Request


app = FastAPI()


@app.get('/')
async def get_request(request: Request):
    return {'path': request.url.path}
