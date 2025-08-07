import logging
from typing import Annotated

from fastapi import FastAPI, Depends, BackgroundTasks
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from app.rate_limiter import limiter

from app.dependencies import time_range, select_category, check_coupon
from app.middleware import ClientInfoMiddleware
from app.profiler import ProfileEndpontMiddleware
from app import internationalization
from app.background_tasks import stor_query_to_external_db

logger = logging.getLogger('uvicorn.error')


app = FastAPI()


app.include_router(internationalization.router)

app.add_middleware(ClientInfoMiddleware)
app.add_middleware(ProfileEndpontMiddleware)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)


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
    background_tasks: BackgroundTasks,
    category: Annotated[select_category, Depends()],
    discount: Annotated[bool, Depends(check_coupon)]
):
    category = category.replace('-', ' ').title()
    message = f'You requested {category}'

    if discount:
        message += 'The coupon code is valid, you will get the discount'
    background_tasks.add_task(
        stor_query_to_external_db, message
    )
    logger.info(
        'Query sent to background task,'
        'end of request.'
    )
    return message
