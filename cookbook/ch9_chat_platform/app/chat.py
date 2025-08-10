from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.ws_manager import ConnctionManager


connection_manager = ConnctionManager()
templates = Jinja2Templates(directory="templates")

router = APIRouter()


@router.websocket('/chatroom/{username}')
async def chatroom(websocket: WebSocket, username: str):
    await connection_manager.connect(websocket)
    await connection_manager.broadcast(
        f'{username} joined the chatroom',
        exclude=websocket,
    )
    try:
        while True:
            data = await websocket.receive_text()
            await connection_manager.broadcast(
                {'sender': username, 'message': data},
                exclude=websocket,
            )
            await connection_manager.send_personal_message(
                {'sender': 'You', 'message': data},
                websocket,
            )
    except WebSocketDisconnect:
        connection_manager.disconnect(websocket)
        await connection_manager.broadcast(
            {'sender': 'system',
             'message': f'Client #{username} left the chat'}
        )


@router.get("/chatroom/{username}")
async def chatroom_page_endpoint(
    request: Request, username: str
) -> HTMLResponse:
    return templates.TemplateResponse(
        request=request,
        name="chatroom.html",
        context={"username": username},
    )
