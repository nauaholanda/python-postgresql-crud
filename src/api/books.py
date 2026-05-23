from fastapi import APIRouter, HTTPException

from services import book_service
from schemas.book import BookResponse, BookCreate, BookUpdate
from exceptions import BookNotFoundException

router = APIRouter(prefix="/books")

@router.get("/", response_model=list[BookResponse])
def get_all_books():
  return book_service.get_all()

@router.post("/", response_model=BookResponse, status_code=201)
def insert_book(book_data: BookCreate):
  return book_service.create(book_data)

@router.put("/{book_id}", response_model=BookResponse)
def update_book(book_id: int, book_data: BookUpdate):
  try:
    return book_service.update(book_id, book_data)
  except BookNotFoundException as error:
    raise HTTPException(status_code=404, detail=str(error))