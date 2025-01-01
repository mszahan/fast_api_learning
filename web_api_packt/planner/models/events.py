from pydantic import BaseModel
from beanie import Document
from typing import List, Optional

class Event(Document):
    creator: Optional[str] = None
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
    
    class Settings:
        name = 'events'
    


class EventUpdate(BaseModel):
    title: Optional[str] = None
    image: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[List[str]] = None
    location: Optional[str] = None
    
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
