from unittest.mock import MagicMock, patch
import pytest

from src.repositories.book_repository import BookRepository
from src.entities.book import Book

@pytest.fixture
def book_repository():
  return BookRepository()

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
