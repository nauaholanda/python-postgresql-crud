from repositories import BookRepository
from schemas.book import BookResponse, BookCreate, BookUpdate
from entities import Book

def get_all() -> list[BookResponse]:
  book_repository = BookRepository()
  books = book_repository.select()
  books_response = [BookResponse.model_validate(book) for book in books]
  return books_response

def create(book_data: BookCreate) -> BookResponse:
  book_repository = BookRepository()
  book = Book(**book_data.model_dump())
  book_repository.insert(book)
  return BookResponse.model_validate(book)

def update(book_id: int, book_data: BookUpdate) -> BookResponse:
  book_repository = BookRepository()
  update_data = book_data.model_dump(exclude_unset=True)
  book = book_repository.update(book_id, update_data)
  return BookResponse.model_validate(book)

def delete(book_id: int) -> None:
  book_repository = BookRepository()
  book_repository.delete(book_id)