from fastapi import FastAPI


app = FastAPI()
# To start app cd into dir then: uvicorn app_name:app --reload


BOOKS = [
    {'title': 'The secret of the old clock', 'author': 'Carolyn Keene', 'category': 'adventure'},
    {'title': 'The hidden staircase', 'author': 'Carolyn Keene', 'category': 'adventure'},
    {'title': 'Halt\'s Peril', 'author': 'John Flanagan', 'category': 'adventure'},
    {'title': 'Fourth Wing', 'author': 'Rebecca Yarros', 'category': 'fantasy'},
    {'title': 'Iron Flame', 'author': 'Rebecca Yarros', 'category': 'fantasy'},
]


@app.get('/books')
async def read_all_books():
    return BOOKS