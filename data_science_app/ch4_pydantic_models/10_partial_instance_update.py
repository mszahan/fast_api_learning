from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, status


class PostBase(BaseModel):
    title: str
    content: str


class PostCreate(PostBase):
    pass


class PostUpdate(BaseModel):
    title: str | None = None
    content: str | None = None


class PostRead(PostBase):
    id: int


class Post(PostBase):
    id: int
    nb_views: int = 0


app = FastAPI()


@app.patch('/posts/{id}', response_model=PostRead)
async def partial_update(id: int, post_update: PostUpdate):
    try:
        post_db = 'db.postst[id]'
        updated_fields = post_update.model_dump(exclude_unset=True)
        updated_post = post_db.copy(update=updated_fields)
        # db.posts[id] = updated_post
        return updated_post
    except KeyError:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
