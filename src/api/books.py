from fastapi import APIRouter

from services import book_service
from schemas.book import BookResponse

router = APIRouter(prefix="/books")

@router.get("/", response_model=list[BookResponse])
def get_all_books():
  return book_service.get_all()