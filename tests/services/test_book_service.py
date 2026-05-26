from unittest.mock import patch, MagicMock, call
import pytest

from entities import Book
from services import book_service
from schemas.book import BookCreate, BookUpdate

@pytest.fixture
def mock_book_repository():
  book_repository = MagicMock()
  with patch("services.book_service.BookRepository") as MockBookRepository:
    MockBookRepository.return_value = book_repository
    yield book_repository

class TestGetAllBooks:
  def test_get_all_books_successfully(self, mock_book_repository):
    db_books = [MagicMock(spec=Book), MagicMock(spec=Book)]
    parsed_books = [MagicMock(), MagicMock()]

    mock_book_repository.select.return_value = db_books

    with patch("services.book_service.BookResponse") as MockBookResponse:
      MockBookResponse.model_validate.side_effect = parsed_books

      response = book_service.get_all()

    assert response == parsed_books
    mock_book_repository.select.assert_called_once()
    MockBookResponse.model_validate.assert_has_calls([call(b) for b in db_books])

class TestCreateBook:
  def test_create_book_successfully(self, mock_book_repository):
    book_data = BookCreate(title="Book title", author="Author name", rating=10)
    parsed_book = MagicMock()

    with patch("services.book_service.Book") as MockBook, \
      patch("services.book_service.BookResponse") as MockBookResponse:

      MockBookResponse.model_validate.return_value = parsed_book

      response = book_service.create(book_data)

    assert response == parsed_book
    MockBook.assert_called_once_with(**book_data.model_dump())
    mock_book_repository.insert.assert_called_once_with(MockBook.return_value)
    MockBookResponse.model_validate.assert_called_once_with(MockBook.return_value)

class TestUpdateBook:
  def test_update_book_successfully(self, mock_book_repository):
    book_id = 1
    book_data = BookUpdate(title="New title")  # ajuste os campos conforme seu schema
    parsed_book = MagicMock()
    updated_book = MagicMock(spec=Book)

    mock_book_repository.update.return_value = updated_book

    with patch("services.book_service.BookResponse") as MockBookResponse:
      MockBookResponse.model_validate.return_value = parsed_book

      response = book_service.update(book_id, book_data)

    assert response == parsed_book
    mock_book_repository.update.assert_called_once_with(book_id, book_data.model_dump(exclude_unset=True))
    MockBookResponse.model_validate.assert_called_once_with(updated_book)