from pydantic import BaseModel
from typing import List, Optional
from fastapi import Form


class Todo(BaseModel):
    id: int
    item: str

    @classmethod
    def as_form(
        cls,
        item: str = Form(...)
    ):
        return cls(item=item)

    ## example schema to show in documentation
    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "item": "This is an example schema"
            }
        }


class TodoItem(BaseModel):
    item: str

    class Config:
        schema_extra = {
            "example": {
                "item": "Read the next chapter of the book"
            }
        }


##so the todo will be without id just item
class TodoItems(BaseModel):
    todos: List[TodoItem]

    class Config:
        schema_extra = {
            'example': {
                'todos': [
                    {"item": "Example schema 1"},
                    {"item": "Example schema 2"}
                ]
            }
        }