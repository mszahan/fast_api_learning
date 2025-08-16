import logging
from fastapi import FastAPI, Body, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from contextlib import asynccontextmanager
from starlette.middleware import Middleware
from middleware.request_middleware import HashBodyMiddleware
from middleware.asgi_middleware import ASGIMiddleware
from middleware.response_middleware import HeaderResponseMiddleware
from middleware.webhook import WebhookSenderMiddleware


logger = logging.getLogger('uvicorn')


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield {'webhook_urls': []}


app = FastAPI(
    title='Middleware Application',
    lifespan=lifespan,
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
app.add_middleware(WebhookSenderMiddleware)


@app.get('/')
async def read_root():
    return {'Hello': 'World'}


@app.post('/send')
async def send(message: str = Body()):
    logger.info(f'Message: {message}')
    return {'message': message}


@app.post('/register-webhook-url')
async def add_webhook_url(request: Request, url: str = Body()):
    if not url.startswith('http'):
        url = f'http://{url}'
    request.state.webhook_urls.append(url)
    return {'url added': url}
