from unittest.mock import patch, MagicMock, call
import pytest

from exceptions import BookNotFoundException
from services import review_service
from entities import Book, Review
from schemas.review import ReviewCreate

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

  def test_raises_exception_when_book_not_found(self, mock_book_repository, mock_review_repository):
    book_id = 1
    mock_book_repository.find_by_id.return_value = None

    with pytest.raises(BookNotFoundException):
      review_service.get_all_by_book_id(book_id)

    mock_review_repository.find_all_by_book_id.assert_not_called()

class TestCreateReview:
  def test_create_review_successfully(self):
    book_id = 1
    review_data = MagicMock(spec=ReviewCreate)
    review_data.model_dump.return_value = { "review_text": "Review", "reviewer_name": "Reviewer" }
    parsed_review = MagicMock()

    with patch("services.review_service.ReviewResponse") as MockReviewResponse:
      MockReviewResponse.model_validate.return_value = parsed_review
      response = review_service.create(book_id, review_data)

    assert response == parsed_review
  
  def test_raises_exception_when_book_not_found(self, mock_book_repository, mock_review_repository):
    book_id = 1
    review_data = MagicMock(spec=ReviewCreate)
    mock_book_repository.find_by_id.return_value = None

    with pytest.raises(BookNotFoundException):
      review_service.create(book_id, review_data)

    mock_review_repository.find_all_by_book_id.assert_not_called()