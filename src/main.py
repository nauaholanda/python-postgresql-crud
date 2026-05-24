from fastapi import FastAPI

from api import books, reviews

app = FastAPI()

app.include_router(books.router)
app.include_router(reviews.router)