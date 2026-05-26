from unittest.mock import patch, MagicMock, call
import pytest

from services import review_service
from entities import Book, Review

@pytest.fixture
def mock_book():
  book = MagicMock(spec=Book)
  return book

@pytest.fixture
def mock_book_repository():
  book_repository = MagicMock()
  with patch("services.review_service.BookRepository") as MockBookRepository:
    MockBookRepository.return_value = book_repository
    yield book_repository

@pytest.fixture
def mock_review_repository():
  review_repository = MagicMock()
  with patch("services.review_service.ReviewRepository") as MockReviewRepository:
    MockReviewRepository.return_value = review_repository
    yield review_repository


class TestGetAllReviewsByBookId:
  def test_get_all_reviews_successfully(self, mock_book, mock_book_repository, mock_review_repository):
    book_id = 1
    db_reviews = [MagicMock(spec=Review), MagicMock(spec=Review)]
    parsed_reviews = [MagicMock(), MagicMock()] 

    mock_book_repository.find_by_id.return_value = mock_book
    mock_review_repository.find_all_by_book_id.return_value = db_reviews

    with patch("services.review_service.ReviewResponse") as MockReviewResponse:
        MockReviewResponse.model_validate.side_effect = parsed_reviews

        response = review_service.get_all_by_book_id(book_id)

    assert response == parsed_reviews
    mock_review_repository.find_all_by_book_id.assert_called_once_with(book_id)
    MockReviewResponse.model_validate.assert_has_calls([call(r) for r in db_reviews])
