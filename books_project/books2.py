from fastapi import FastAPI


app = FastAPI()


BOOKS = []


@app.get('/books')
async def read_books():
    """Get all books"""
    return BOOKS
