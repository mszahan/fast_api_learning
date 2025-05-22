import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI
import models
from database import engine
from routers import auth, todos, admin, users


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get('/healthy')
def check_health():
    return {'status': 'Healthy'}


app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)
