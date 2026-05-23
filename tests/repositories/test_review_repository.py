from unittest.mock import MagicMock, patch
import pytest

from src.repositories.review_repository import ReviewRepository
from src.entities.review import Review

@pytest.fixture
def repository() -> ReviewRepository:
  return ReviewRepository()

@pytest.fixture
def mock_review():
  review = MagicMock(spec=Review)
  review.book_id = 1
  return review

@pytest.fixture
def mock_db_session():
  mock_db = MagicMock()
  mock_session = MagicMock()
  mock_db.session = mock_session
  return mock_db, mock_session

class TestFindAllReviewsByBookId:
  def test_returns_book_reviews(self, repository: ReviewRepository, mock_db_session):
    mock_db, mock_session = mock_db_session
    expected_response = [MagicMock(spec=Review), MagicMock(spec=Review)]

    mock_session.query.return_value.filter.return_value.all.return_value = expected_response

    with patch("src.repositories.review_repository.DBConnection") as MockDBConnection:
      MockDBConnection.return_value.__enter__.return_value = mock_db
      response = repository.find_all_by_book_id(1)

    assert response == expected_response

  def test_returns_empty_list_when_reviews_dont_exist(self, repository: ReviewRepository, mock_db_session):
    mock_db, mock_session = mock_db_session

    mock_session.query.return_value.filter.return_value.all.return_value = []

    with patch("src.repositories.review_repository.DBConnection") as MockDBConnection:
      MockDBConnection.return_value.__enter__.return_value = mock_db
      response = repository.find_all_by_book_id(1)

    assert response == []

class TestInsertReview:
  def test_successfully_insert_review(self, repository: ReviewRepository, mock_review, mock_db_session):
    mock_db, mock_session = mock_db_session

    with patch("src.repositories.review_repository.DBConnection") as MockDBConnection:
      MockDBConnection.return_value.__enter__.return_value = mock_db

      repository.insert(mock_review)

    mock_session.add.assert_called_once_with(mock_review)
    mock_session.commit.assert_called_once()
    mock_session.rollback.assert_not_called()
  
  def test_rollback_when_raise_exception(self, repository: ReviewRepository, mock_review, mock_db_session):
    mock_db, mock_session = mock_db_session
    mock_session.commit.side_effect = Exception("Error")

    with patch("src.repositories.review_repository.DBConnection") as MockDBConnection:
      MockDBConnection.return_value.__enter__.return_value = mock_db

      with pytest.raises(Exception, match="Error"):
        repository.insert(mock_review)

    mock_session.rollback.assert_called_once()
