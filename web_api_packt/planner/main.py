from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from database.connection import Settings
from database.connection import Settings

from routes.users import user_router
from routes.events import event_router

import uvicorn

settings = Settings()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    await settings.initialize_database()     
    yield

app = FastAPI(lifespan=lifespan)    

## register routes
app.include_router(user_router, prefix='/user')
app.include_router(event_router, prefix='/event')


# origins = [
#  "http://packtpub.com",
#  "https://packtpub.com"
# ]

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8080, reload=True)
