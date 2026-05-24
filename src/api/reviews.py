from fastapi import APIRouter

from services import review_service
from schemas.review import ReviewResponse

router = APIRouter(prefix="/books/{book_id}/reviews")

@router.get("/", response_model=list[ReviewResponse])
def get_all_reviews_by_book_id(book_id: int):
  return review_service.get_all_by_book_id(book_id)