from pydantic import BaseModel
from typing import List

class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tags: List [str]
    location: str

    class Config:
        json_schema_extra = {
            "example": {
                "title": "FastApi book Launch",
                "image": "https://image.com/image.png",
                "description": "the even will be on launching the new book",
                "tags": ["python", "fasapi", "book", "launch"],
                "location": "Google Meet"
            }
        }