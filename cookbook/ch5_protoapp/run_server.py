import uvicorn
from protoapp.main import app


if __name__ == '__main__':
    uvicorn.run(app, reload=True)
