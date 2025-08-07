from fastapi import FastAPI, WebSocket


app = FastAPI()


@app.websocket('/ws')
async def we_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_text(
        'welcome to fastapi chatroom'
    )
    await websocket.close()
