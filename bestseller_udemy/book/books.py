from fastapi import FastAPI


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

@app.get('/books/{book_title}')
async def read_book(book_title:str):
    for book in BOOK:
        if book['title'].casefold() == book_title.casefold():
            return book
