import string

from fastapi import FastAPI


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


BOOKS = [
    Book(1, "Computer Science Pro", "Coding with Roby", "A great book", 5),
    Book(2, "Be fast with FastAPI", "Coding with Roby", "A very nice book", 5),
    Book(3, "Master Endpoints", "Coding with Roby", "An awesome book", 5),
    Book(4, "HP1", "Author 1", "Book description", 2),
    Book(5, "HP2", "Author 2", "Book description", 3),
    Book(6, "HP3", "Author 3", "Book description", 1),
]


@app.get('/books')
async def read_books():
    """Get all books"""
    return BOOKS


