import logging
from fastapi import FastAPI, WebSocket


logger = logging.getLogger('uvicorn')

app = FastAPI()


@app.websocket('/ws')
async def we_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_text(
        'welcome to fastapi chatroom'
    )
    while True:
        data = await websocket.receive_text()
        logger.info(f'Message recieved: {data}')
        await websocket.send_text('message recieved')
    # await websocket.close()
