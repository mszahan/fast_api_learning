# from pydantic import BaseModel
from typing import List, Optional
from sqlmodel import JSON, Field, Column, SQLModel


class Event(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    image: str
    description: str
    tags: List [str] = Field(sa_column=Column(JSON))
    location: str

    class Config:
        arbitrary_types_allowed = True
        json_schema_extra = {
            "example": {
                "title": "FastApi book Launch",
                "image": "https://image.com/image.png",
                "description": "the even will be on launching the new book",
                "tags": ["python", "fasapi", "book", "launch"],
                "location": "Google Meet"
            }
        }


class EventUpdate(SQLModel):
    title: Optional[str]
    image: Optional[str]
    description: Optional[str]
    tags: Optional[List[str]]
    location: Optional[str]

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