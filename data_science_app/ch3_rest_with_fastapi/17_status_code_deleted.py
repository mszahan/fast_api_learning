from fastapi import FastAPI, status
from pydantic import BaseModel


class Post(BaseModel):
    title: str
    nb_views: int


# dummy db
posts = {
    1: Post(title='hello', nb_views=100)
}

app = FastAPI()


@app.delete('/posts/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int):
    posts.pop(id, None)
    return None
