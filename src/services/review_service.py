from schemas.review import ReviewResponse
from repositories import ReviewRepository, BookRepository
from exceptions import BookNotFoundException

def get_all_by_book_id(book_id: int) -> list[ReviewResponse]:
  validate_book_exists(book_id)
  review_repository = ReviewRepository()
  book_reviews = review_repository.find_all_by_book_id(book_id)
  reviews_response = [ReviewResponse.model_validate(review) for review in book_reviews]
  return reviews_response

def validate_book_exists(book_id: int) -> None:
  book_repository = BookRepository()
  book = book_repository.find_by_id(book_id)
  if book is None: 
    raise BookNotFoundException(f"Book with ID {book_id} not found.")