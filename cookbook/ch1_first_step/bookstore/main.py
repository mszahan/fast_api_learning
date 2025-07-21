from fastapi import FastAPI


app = FastAPI()


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
