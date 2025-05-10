from fastapi import FastAPI, Body

app = FastAPI()



class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

books = [
    Book(1, 'Web api with fastapi', 'dakota', 'fastapi beginer book', 4),
    Book(2, 'Farm stack web development', 'alex', 'full stack fastapi book', 5),
    Book(3, 'django 5 by example', 'luna', 'Advanced django book from packt', 5),
    Book(4, 'Learning python', 'rebecca', 'python book for beginner', 4),
    Book(5, 'OOP with python', 'dakota', 'Objec oriented programming in python', 5),
    Book(6, 'Mastering python', 'alex', 'Advanced book of python', 4),
]
        


@app.get('/books')
async def book_list():
    return books


@app.post('/create-book')
async def creat_book(request_book=Body()):
    books.append(request_book)