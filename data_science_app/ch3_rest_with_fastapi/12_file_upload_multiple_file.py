from fastapi import FastAPI, UploadFile, File


app = FastAPI()


@app.post('/files')
async def upload_multiple_files(files: list[UploadFile] = File(...)):
    return [
        {'file name': file.filename, 'content type': file.content_type}
        for file in files
    ]
