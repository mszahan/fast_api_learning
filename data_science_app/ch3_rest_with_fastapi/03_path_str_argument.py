from fastapi import FastAPI, Path

app = FastAPI()


@app.get('/license-plates/{license}')
async def get_liscence_plate(license: str = Path(..., min_length=9, max_length=15)):
    return {'license': license}
