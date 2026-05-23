from fastapi import FastAPI
import models
from database import engine
from routers import auth, todos


app = FastAPI()

# This only runs if the db doesn't exist yet!
models.Base.metadata.create_all(bind=engine)


# Add router
app.include_router(auth.router)
app.include_router(todos.router)
