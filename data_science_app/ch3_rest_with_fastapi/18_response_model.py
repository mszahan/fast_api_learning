from fastapi import FastAPI
from pydantic import BaseModel


class Post(BaseModel):
    title: str
    nb_views: int


class PublicPost(BaseModel):
    title: str


# dummy db
posts = {
    1: Post(title='hello', nb_views=100)
}


app = FastAPI()


@app.get('/posts/{id}', response_model=PublicPost)
async def get_post(id: int):
    return posts[id]
