from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()



class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published: int

    def __init__(self, id, title, author, description, rating, published):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published = published

class BookRequest(BaseModel):
    # id: Optional[int] = None
    id: Optional[int] = Field(description='ID is not needed on create', default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=3)
    description: str = Field(min_length=5, max_length=100)
    rating: int = Field(gt=0, lt=6)
    published: int = Field(gt=1999, lt=2030)

    # this is just for the schema on the documentation
    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "python for everybody",
                "author": "Dr. chuck",
                "description": "Python beginner friendly book",
                "rating": 5,
                "published":2004
            }
        }
    }


books = [
    Book(1, 'Web api with fastapi', 'dakota', 'fastapi beginer book', 4, 2002),
    Book(2, 'Farm stack web development', 'alex', 'full stack fastapi book', 5, 2005),
    Book(3, 'django 5 by example', 'luna', 'Advanced django book from packt', 5, 2000),
    Book(4, 'Learning python', 'rebecca', 'python book for beginner', 4, 2002),
    Book(5, 'OOP with python', 'dakota', 'Objec oriented programming in python', 5, 2005),
    Book(6, 'Mastering python', 'alex', 'Advanced book of python', 4, 2004),
]
        
def handle_book_id(book: Book):
    # if len(books) > 0:
    #     book.id = books[-1].id +1
    # else:
    #     book.id = 1
    book.id = 1 if len(books) == 0 else books[-1].id + 1
    return book

@app.get('/books')
async def book_list():
    return books


@app.get('/books/{book_id}')
async def book_detail(book_id: int = Path(gt=0)):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail='No book found')


@app.get('/books-rating') # /books will override the book_list endpoint and /books/something will behave differently for param in book detail
async def book_by_rating(book_rating: int = Query(gt=0, lt=6)):
    book_list = []
    for book in books:
        if book.rating == book_rating:
            book_list.append(book)
    return book_list


@app.get('/books-published')
async def book_by_pulished(published: int = Query(gt=1999, lt=2030)):
    book_list = []
    for book in books:
        if book.published == published:
            book_list.append(book)
    return book_list


@app.post('/create-book')
async def creat_book(request_book: BookRequest):
    new_book = Book(**request_book.model_dump())
    new_book = handle_book_id(new_book)
    books.append(new_book)


@app.put('/books/update-book')
async def update_book(book: BookRequest):
    book_changed = False
    for n in range(len(books)):
        if books[n].id == book.id:
            books[n] = book
            book_changed = True
    if not book_changed:
        raise HTTPException(status_code=404, detail='No book found to update')


@app.delete('/books/{book_id}')
async def delete_book(book_id: int = Path(gt=0)):
    book_deleted = False
    for n in range(len(books)):
        if books[n].id == book_id:
            books.pop(n)
            book_deleted = True
            break
    if not book_deleted:
        raise HTTPException(status_code=404, detail= 'No book found')