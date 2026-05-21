from unittest.mock import MagicMock
import pytest

from src.repositories.review_repository import ReviewRepository

@pytest.fixture
def repository() -> ReviewRepository:
  return ReviewRepository()

@pytest.fixture
def mock_db_session():
  mock_db = MagicMock()
  mock_session = MagicMock()
  mock_db.session = mock_session
  return mock_db, mock_session
