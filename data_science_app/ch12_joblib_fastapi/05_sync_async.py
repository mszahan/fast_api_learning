import time
import asyncio
from fastapi import FastAPI

app = FastAPI()


@app.get('/fast')
async def fast():
    return {'endpoint': 'fast'}


@app.get('/fast-sync')
def fast_sync():
    return {'endpoint': 'fast'}


@app.get('/slow-async')
def slow_async():
    """Runs in the main process"""
    time.sleep(10)  # blocking sync operation
    print('10 seconds done')
    return {'endpoint': 'slow-async'}

# @app.get('/slow-async')
# async def slow_async():
#     """Runs in the main process"""
#     await asyncio.sleep(10)  # blocking async operation
#     print('10 seconds done')
#     return {'endpoint': 'slow-async'}


@app.get('/slow-sync')
def slow_sync():
    """Runs in a thread"""
    time.sleep(10)  # blocking sync operation
    return {'endpoint': 'slow-sync'}
