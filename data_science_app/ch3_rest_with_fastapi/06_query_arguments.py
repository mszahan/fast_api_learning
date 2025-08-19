from fastapi import FastAPI, Query

app = FastAPI()


@app.get('/users')
async def get_user(page: int = Query(1, gt=0), size: int = Query(10, 100)):
    return {'page': page, 'size': size}
