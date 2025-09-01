from datetime import datetime
from bson import ObjectId
from pydantic import BaseModel, Field, BeforeValidator, ConfigDict
from typing import Annotated


# ObjectId type that validates and appears as string in OpenAPI
PyObjectId = Annotated[
    str,
    BeforeValidator(lambda v: str(v) if isinstance(v, ObjectId) else v),
]


class MongoBaseModel(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str}
    )

    id: PyObjectId = Field(
        default_factory=lambda: str(ObjectId()), alias="_id")


class PostBase(MongoBaseModel):
    title: str
    content: str
    publication_date: datetime = Field(default_factory=datetime.now)


class PostPartialUpdate(BaseModel):
    title: str | None = None
    content: str | None = None


class PostCreate(PostBase):
    pass


class Post(PostBase):
    pass
