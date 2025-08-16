import logging
from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from starlette.middleware import Middleware
from middleware.request_middleware import HashBodyMiddleware
from middleware.asgi_middleware import ASGIMiddleware
from middleware.response_middleware import HeaderResponseMiddleware


logger = logging.getLogger('uvicorn')


app = FastAPI(
    title='Middleware Application',
    middleware=[
        Middleware(ASGIMiddleware, parameter='example_parameter')
    ]
)

app.add_middleware(HashBodyMiddleware, allowed_paths=['/send'])
app.add_middleware(HeaderResponseMiddleware,
                   headers=(
                       ('new-header', 'fastapi-cookbook'),
                       ('another-header', 'another-value')
                   ))

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*']
)

app.add_middleware(TrustedHostMiddleware, allowed_hosts=['localhost'])


@app.get('/')
async def read_root():
    return {'Hello': 'World'}


@app.post('/send')
async def send(message: str = Body()):
    logger.info(f'Message: {message}')
    return {'message': message}
