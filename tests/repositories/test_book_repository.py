from unittest.mock import MagicMock
import pytest

from src.repositories.book_repository import BookRepository

@pytest.fixture
def book_repository():
  return BookRepository()

@pytest.fixture
def mock_db_session():
  mock_db = MagicMock()
  mock_session = MagicMock()
  mock_db.session = mock_session
  return mock_db, mock_session