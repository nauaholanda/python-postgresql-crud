from repositories import BookRepository
from schemas.book import BookResponse, BookCreate
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