import logging
from typing import Annotated
from fastapi import (FastAPI, WebSocket, WebSocketDisconnect,
                     WebSocketException, status, Depends)
from app.chat import router as chat_router
from app.security import get_username_from_token


logger = logging.getLogger('uvicorn')

app = FastAPI()

app.include_router(chat_router)


@app.websocket('/ws')
async def we_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_text(
        'welcome to fastapi chatroom'
    )
    try:
        while True:
            data = await websocket.receive_text()
            logger.info(f'Message recieved: {data}')
            await websocket.send_text(f'message recieved - {data}')
            if data == 'disconnect':
                logger.warning('Connection closed by server')
                return await websocket.close(
                    code=status.WS_1000_NORMAL_CLOSURE,
                    reason='Disconnecting...'
                )
                # await websocket.close()
                # break
            if 'bad message' in data:
                raise WebSocketException(
                    code=status.WS_1008_POLICY_VIOLATION,
                    reason='Inappropriate message'
                )
    except WebSocketDisconnect:
        logger.warning('Connection closed by client')
    # await websocket.close()


@app.websocket('/secured-ws')
async def secured_websocket(
    websocket: WebSocket,
    username: Annotated[get_username_from_token, Depends()]
):
    await websocket.accept()
    await websocket.send_text(f'Welcome {username}')
    async for data in websocket.iter_text():
        await websocket.send_text(f'You wrote: {data}')
