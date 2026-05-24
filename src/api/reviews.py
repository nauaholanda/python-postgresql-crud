from fastapi import APIRouter

from services import review_service
from schemas.review import ReviewResponse, ReviewCreate

router = APIRouter(prefix="/books/{book_id}/reviews")

@router.get("/", response_model=list[ReviewResponse])
def get_all_reviews_by_book_id(book_id: int):
  return review_service.get_all_by_book_id(book_id)

@router.post("/", response_model=ReviewResponse)
def insert_review_to_a_book(book_id: int, review_data: ReviewCreate):
  return review_service.create(book_id, review_data)