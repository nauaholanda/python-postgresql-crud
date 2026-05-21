from unittest.mock import MagicMock, patch
import pytest

from src.repositories.review_repository import ReviewRepository
from src.entities.review import Review

@pytest.fixture
def repository() -> ReviewRepository:
  return ReviewRepository()

@pytest.fixture
def mock_db_session():
  mock_db = MagicMock()
  mock_session = MagicMock()
  mock_db.session = mock_session
  return mock_db, mock_session

class TestFindAllByBookId:
  def test_returns_book_reviews(self, repository: ReviewRepository, mock_db_session):
    mock_db, mock_session = mock_db_session
    expected_response = [MagicMock(spec=Review), MagicMock(spec=Review)]

    mock_session.query.return_value.filter.return_value.all.return_value = expected_response

    with patch("src.repositories.review_repository.DBConnection") as MockDBConnection:
      MockDBConnection.return_value.__enter__.return_value = mock_db
      response = repository.find_all_by_book_id(1)

    assert response == expected_response
