from datetime import datetime
from pydantic import BaseModel, Field


def list_factory():
    return ['a', 'b', 'c']


class Model(BaseModel):
    # You simply have to pass a function to this argument. Don’t put arguments on it
    book_list: list[str] = Field(default_factory=list_factory)
    time: datetime = Field(default_factory=datetime.now)
    other_list: list[str] = Field(default_factory=list)
