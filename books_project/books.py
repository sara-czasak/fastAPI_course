from fastapi import FastAPI, Body


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


@app.get('/books/')
async def read_by_category_query(category: str):
    """Get books by category"""
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get('/books/{book_author}/')
async def read_author_category_by_query(book_author: str, category: str):
    """Get books by author and category"""
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.post("/books/create_book")
async def create_book(new_book=Body()):
    """Add a new book"""
    BOOKS.append(new_book)


@app.put('/books/update_book')
async def update_book(updated_book=Body()):
    """Update a book by book title"""
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book