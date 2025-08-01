from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from typing import Any
from models import Book, BookResponse, UserIn, UserOut, BaseUser, CreateUser


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


app = FastAPI()

# setting custom response


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={
            'message': f'Unicorns are not real: {exc.name}',
        }
    )


@app.get('/books/{book_id}')
async def read_book(book_id: int):
    return {
        'book_id': book_id,
        'title': 'Sample Book Title',
        'author': 'Sample Author',
    }


@app.get('/authors/{author_id}')
async def read_author(author_id: int):
    return {
        'author_id': author_id,
        'name': 'Sample Author Name',
        'books': ['Sample Book Title 1', 'Sample Book Title 2'],
    }


@app.get('/books')
async def read_books(year: int = None):
    if year:
        return {
            'year': year,
            'books': ['Sample Book Title 1', 'Sample Book Title 2'],
        }
    return {'books': ['all books']}


# path parameters with path paramters within it
@app.get('/filse/{file_path:path}')
async def read_file(file_path: str):
    return {
        'file_path': file_path,
        'message': 'File path received successfully',
    }


@app.post('/book')
async def create_book(book: Book):
    return book


@app.get('/allbooks', response_model=list[BookResponse])
# async def read_all_books() -> list[BookResponse]:
async def read_all_books():
    return [
        {'title': 'Sherlock Holmes', 'author': 'Arthur Conan Doyle'},
        {'title': '1984', 'author': 'George Orwell'},
    ]


# use different response models for input and output to hide the password
@app.post('/user', response_model=UserOut)
async def create_user(user: UserIn) -> Any:
    return user


# another way to use different response models for input and output
@app.post('/user/create')
async def create_user(user: CreateUser) -> BaseUser:
    return user


# raising custom exception
@app.get('/unicorns/{name}')
async def get_unicorn(name: str):
    if name == 'yelo':
        raise UnicornException(name=name)
    return {'unicorn_name': name, 'message': 'Unicorn is real!'}
