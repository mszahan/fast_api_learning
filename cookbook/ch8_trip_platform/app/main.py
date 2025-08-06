from typing import Annotated
from fastapi import FastAPI, Depends
from app.dependencies import time_range, select_category, check_coupon

app = FastAPI()


@app.get('/v1/trips')
# same as the latter one
# def get_tours(time: Anotated[time_range, Depends()])
def get_tours(time=Depends(time_range)):
    start, end = time
    message = f'Request trips from {start}'
    if end:
        return f'{message} to {end}'
    return message


@app.get('/v2/trips/{category}')
def get_trips_by_category(
    category: Annotated[select_category, Depends()],
    discount: Annotated[bool, Depends(check_coupon)]
):
    category = category.replace('-', ' ').title()
    message = f'You requested {category}'

    if discount:
        message += 'The coupon code is valid, you will get the discount'
    return message
