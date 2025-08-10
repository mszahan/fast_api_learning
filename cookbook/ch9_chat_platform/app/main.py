import logging
from fastapi import FastAPI, WebSocket, WebSocketDisconnect


logger = logging.getLogger('uvicorn')

app = FastAPI()


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
                await websocket.close()
                break
    except WebSocketDisconnect:
        logger.warning('Connection closed by client')
    # await websocket.close()
