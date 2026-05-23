from repositories import BookRepository
from schemas.book import BookResponse

def get_all() -> list[BookResponse]:
  book_repository = BookRepository()
  books = book_repository.select()
  books_response = [BookResponse.model_validate(book) for book in books]
  return books_response