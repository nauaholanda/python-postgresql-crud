from fastapi import APIRouter

from services import book_service
from schemas.book import BookResponse, BookCreate

router = APIRouter(prefix="/books")

@router.get("/", response_model=list[BookResponse])
def get_all_books():
  return book_service.get_all()

@router.post("/", response_model=BookResponse, status_code=201)
def insert_book(book_data: BookCreate):
  return book_service.create(book_data)