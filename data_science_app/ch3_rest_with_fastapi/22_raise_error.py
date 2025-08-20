from fastapi import FastAPI, Body, HTTPException, status


app = FastAPI()


@app.post('/password')
async def check_password(password: str = Body(...), password_confirm: str = Body(...)):
    if password != password_confirm:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Password did not match'
        )
    return {'message': 'password matched'}
