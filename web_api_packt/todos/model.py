from pydantic import BaseModel


class Todo(BaseModel):
    id: int
    item: str
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