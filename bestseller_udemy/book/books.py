from fastapi import FastAPI, Body


app = FastAPI()

BOOK = [
    {'title':'Title one', 'author': 'author one', 'category': 'Science'},
    {'title':'Title two', 'author': 'author two', 'category': 'Science'},
    {'title':'Title three', 'author': 'author three', 'category': 'history'},
    {'title':'Title four', 'author': 'author four', 'category': 'math'},
    {'title':'Title five', 'author': 'author five', 'category': 'math'},
    {'title':'Title six', 'author': 'author six', 'category': 'math'},
    {'title':'favorite book', 'author': 'myself', 'category': 'python'},
]

@app.get('/books')
async def read_all_books():
    return BOOK

# to make it work within dynamic parameter it needs to be on top
@app.get('/books/favorite-book')
async def favorite_book():
    return BOOK[-1]

# path parameter
@app.get('/books/{book_title}')
async def read_book(book_title:str):
    for book in BOOK:
        if book['title'].casefold() == book_title.casefold():
            return book

# just query parameter
@app.get('/book')
async def book_by_category(category:str):
    book_list = []
    for book in BOOK:
        if book.get('category').casefold() == category.casefold():
            book_list.append(book)
    return book_list

# with both path and query parameter
@app.get('/book/{author_name}')
async def book_by_author_category(author_name:str, category:str):
    book_list = []
    for book in BOOK:
        if book.get('author').casefold() == author_name.casefold() and \
            book.get('category').casefold() == category.casefold():
            book_list.append(book)
    return book_list

@app.post('/books/create-book')
async def create_book(newbook=Body()):
    BOOK.append(newbook)

