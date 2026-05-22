from fastapi import FastAPI


app = FastAPI()
# To start app cd into dir then: uvicorn app_name:app --reload


BOOKS = [
    {'title': 'The secret of the old clock', 'author': 'Carolyn Keene', 'category': 'adventure'},
    {'title': 'The hidden staircase', 'author': 'Carolyn Keene', 'category': 'adventure'},
    {'title': 'Halt\'s Peril', 'author': 'John Flanagan', 'category': 'adventure'},
    {'title': 'Fourth Wing', 'author': 'Rebecca Yarros', 'category': 'fantasy'},
    {'title': 'Iron Flame', 'author': 'Rebecca Yarros', 'category': 'fantasy'},
    {'title': 'Onyx Storm', 'author': 'Rebecca Yarros', 'category': 'fantasy'},
]


@app.get('/books')
async def read_all_books():
    """Get all books"""
    return BOOKS


@app.get('/books/{book_title}')
async def read_book(book_title: str):
    """Get book by book title"""
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book


