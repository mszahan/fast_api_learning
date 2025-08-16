import logging
from starlette.types import ASGIApp, Scope, Receive, Send

logger = logging.getLogger('uvicorn')


class ASGIMiddleware:
    def __init__(self, app: ASGIApp, parameter: str = 'default'):
        self.app = app
        self.parameter = parameter

    async def __call__(self, scope: Scope, receive: Receive, send: Send):
        logger.info('Entering ASGI middleware')
        logger.info(f'The parameter is: {self.parameter}')
        logger.info(f'the event scope: {scope.get("type")}')
        await self.app(scope, receive, send)
        logger.info('Exiting ASGI middleware')
