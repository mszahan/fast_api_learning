from pydantic import BaseModel, Field, EmailStr


class Book(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    author: str = Field(..., min_length=1, max_length=50)
    year: int = Field(..., gt=1900, lt=2025)


class BookResponse(BaseModel):
    title: str
    author: str


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class BaseUser(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class CreateUser(BaseUser):
    password: str
