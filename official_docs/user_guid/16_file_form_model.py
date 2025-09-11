from typing import Annotated
from fastapi import FastAPI, File, Form, UploadFile, Depends
from pydantic import BaseModel


app = FastAPI()


# class FormData(BaseModel):
#     name: str
#     username: str
#     file_a: bytes
#     file_b: UploadFile


# @app.post('/files/')
# async def creat_file(data: Annotated[FormData, Form()]):
#     return {
#         'name': data.name,
#         'username': data.username,
#         'file_a_size': len(data.file_a),
#         'file_b_content_type': data.file_b.content_type
#     }


class FormData(BaseModel):
    name: str
    username: str


def form_dependency(
    name: Annotated[str, Form()],
    username: Annotated[str, Form()],
) -> FormData:
    return FormData(name=name, username=username)


@app.post("/files/")
async def create_file(
    data: Annotated[FormData, Depends(form_dependency)],
    file_a: Annotated[bytes, File()],
    file_b: Annotated[UploadFile, File()],
):
    return {
        "name": data.name,
        "username": data.username,
        "file_a_size": len(file_a),
        "file_b_content_type": file_b.content_type,
    }
