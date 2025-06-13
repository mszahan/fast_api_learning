from fastapi import FastAPI, status


app = FastAPI()

@app.get('/', status_code=status.HTTP_208_ALREADY_REPORTED)
async def fa_status():
    return {"message": "fastapi status code 208"}