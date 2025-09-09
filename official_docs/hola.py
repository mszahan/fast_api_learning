from fastapi import FastAPI


app = FastAPI()


@app.get('/uv')
async def uv():
    return {'hello': 'uv'}
