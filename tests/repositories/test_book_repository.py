from unittest.mock import MagicMock, patch
import pytest

from src.repositories.book_repository import BookRepository
from src.entities.book import Book

@pytest.fixture
def book_repository():
  return BookRepository()

@pytest.fixture
def mock_book():
  book = MagicMock(spec=Book)
  book.title = 'Test Book'
  return book

@pytest.fixture
def mock_db_session():
  mock_db = MagicMock()
  mock_session = MagicMock()
  mock_db.session = mock_session
  return mock_db, mock_session

class TestSelectBooks:
  def test_return_all_books_successfully(self, book_repository: BookRepository, mock_db_session):
    mock_db, mock_session = mock_db_session
    expected = [MagicMock(spec=Book), MagicMock(spec=Book)]

    mock_session.query.return_value.all.return_value = expected

    with patch("src.repositories.book_repository.DBConnection") as MockDBConnection:
      MockDBConnection.return_value.__enter__.return_value = mock_db

      response = book_repository.select()

    assert response == expected

class TestInsertBook:
  def test_insert_book_successfully(self, book_repository: BookRepository, mock_book, mock_db_session):
    mock_db, mock_session = mock_db_session

    with patch("src.repositories.book_repository.DBConnection") as MockDBConnection:
      MockDBConnection.return_value.__enter__.return_value = mock_db

      book_repository.insert(mock_book)

    mock_session.add.assert_called_once_with(mock_book)
    mock_session.commit.assert_called_once()

  def test_rollback_when_raise_exception(self, book_repository: BookRepository, mock_book, mock_db_session):
    mock_db, mock_session = mock_db_session

    mock_session.add.side_effect = Exception("Error")

    with patch("src.repositories.book_repository.DBConnection") as MockDBConnection:
      MockDBConnection.return_value.__enter__.return_value = mock_db

      with pytest.raises(Exception, match="Error"):
        book_repository.insert(mock_book)

    mock_session.add.assert_called_with(mock_book)
    mock_session.commit.assert_not_called()
    mock_session.rollback.assert_called_once()
  
class TestFindBookById:
  def test_find_book_successfully(self, book_repository: BookRepository, mock_book, mock_db_session):
    mock_db, mock_session = mock_db_session

    expected = mock_book
    mock_session.query.return_value.filter.return_value.one.return_value = expected

    with patch("src.repositories.book_repository.DBConnection") as MockDBConnection:
      MockDBConnection.return_value.__enter__.return_value = mock_db

      response = book_repository.find_by_id(1)
    
    assert response == expected
