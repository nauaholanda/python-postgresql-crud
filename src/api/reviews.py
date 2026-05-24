from fastapi import APIRouter, HTTPException

from services import review_service
from schemas.review import ReviewResponse, ReviewCreate
from exceptions import BookNotFoundException

router = APIRouter(prefix="/books/{book_id}/reviews")

@router.get("/", response_model=list[ReviewResponse])
def get_all_reviews_by_book_id(book_id: int):
  try:
    return review_service.get_all_by_book_id(book_id)
  except BookNotFoundException as error:
    raise HTTPException(status_code=404, detail=str(error))

@router.post("/", response_model=ReviewResponse)
def insert_review_to_a_book(book_id: int, review_data: ReviewCreate):
  try:
    return review_service.create(book_id, review_data)
  except BookNotFoundException as error:
    raise HTTPException(status_code=404, detail=str(error))