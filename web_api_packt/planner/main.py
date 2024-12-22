# from contextlib import asynccontextmanager
# from database.connection import init_db
from fastapi import FastAPI
from database.connection import Settings

from routes.users import user_router
from routes.events import event_router

import uvicorn



# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     # Load the ML model
#     await init_db()     
#     yield

app = FastAPI()    

## register routes
app.include_router(user_router, prefix='/user')
app.include_router(event_router, prefix='/event')


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8080, reload=True)
