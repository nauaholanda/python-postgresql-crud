from sqlalchemy.orm.exc import NoResultFound
from unittest.mock import MagicMock, patch
import pytest

from repositories.book_repository import BookRepository
from entities.book import Book
from exceptions import BookNotFoundException

@pytest.fixture
def book_repository():
  return BookRepository()

@pytest.fixture
def mock_book():
  book = MagicMock(spec=Book)
  book.id = 1
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

    with patch("repositories.book_repository.DBConnection") as MockDBConnection:
      MockDBConnection.return_value.__enter__.return_value = mock_db

      response = book_repository.select()

    assert response == expected

class TestInsertBook:
  def test_insert_book_successfully(self, book_repository: BookRepository, mock_book, mock_db_session):
    mock_db, mock_session = mock_db_session

    with patch("repositories.book_repository.DBConnection") as MockDBConnection:
      MockDBConnection.return_value.__enter__.return_value = mock_db

      book_repository.insert(mock_book)

    mock_session.add.assert_called_once_with(mock_book)
    mock_session.commit.assert_called_once()

  def test_rollback_when_raise_exception(self, book_repository: BookRepository, mock_book, mock_db_session):
    mock_db, mock_session = mock_db_session

    mock_session.add.side_effect = Exception("Error")

    with patch("repositories.book_repository.DBConnection") as MockDBConnection:
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

    with patch("repositories.book_repository.DBConnection") as MockDBConnection:
      MockDBConnection.return_value.__enter__.return_value = mock_db

      response = book_repository.find_by_id(1)
    
    assert response == expected

  def test_return_none_when_no_result_found(self, book_repository: BookRepository, mock_db_session):
    mock_db, mock_session = mock_db_session

    mock_session.query.return_value.filter.return_value.one.side_effect = NoResultFound("")

    with patch("repositories.book_repository.DBConnection") as MockDBConnection:
      MockDBConnection.return_value.__enter__.return_value = mock_db

      response = book_repository.find_by_id(1)
    
    assert response is None

class TestDeleteBook:
  def test_delete_book_successfully(self, book_repository: BookRepository, mock_book, mock_db_session):
    mock_db, mock_session = mock_db_session

    mock_session.query.return_value.filter.return_value.first.return_value = mock_book

    with patch("repositories.book_repository.DBConnection") as MockDBConnection:
      MockDBConnection.return_value.__enter__.return_value = mock_db

      response = book_repository.delete(1)

    assert response == mock_book
    mock_session.query.return_value.filter.return_value.delete.assert_called_once()
    mock_session.commit.assert_called_once()

  def test_rollback_and_raise_exception_when_book_not_found(self, book_repository: BookRepository, mock_db_session):
    mock_db, mock_session = mock_db_session

    exception_message = f"Book with ID {1} not found."
    mock_session.query.return_value.filter.return_value.delete.return_value = 0

    with patch("repositories.book_repository.DBConnection") as MockDBConnection:
      MockDBConnection.return_value.__enter__.return_value = mock_db

      with pytest.raises(BookNotFoundException, match=exception_message):
        book_repository.delete(1)

    mock_session.query.return_value.filter.return_value.delete.assert_called_once()
    mock_session.commit.assert_not_called()
    mock_session.rollback.assert_called_once()

  def test_rollback_when_raise_exception(self, book_repository: BookRepository, mock_db_session):
    mock_db, mock_session = mock_db_session

    mock_session.query.return_value.filter.return_value.delete.side_effect = Exception("Error")

    with patch("repositories.book_repository.DBConnection") as MockDBConnection:
      MockDBConnection.return_value.__enter__.return_value = mock_db

      with pytest.raises(Exception, match="Error"):
        book_repository.delete(1)

    mock_session.query.return_value.filter.return_value.delete.assert_called_once()
    mock_session.commit.assert_not_called()
    mock_session.rollback.assert_called_once()

class TestUpdateBook:
  def test_update_book_successfully(self, book_repository: BookRepository, mock_book, mock_db_session):
    mock_db, mock_session = mock_db_session

    mock_session.query.return_value.filter.return_value.update.return_value = 1
    mock_session.query.return_value.filter.return_value.first.return_value = mock_book

    with patch("repositories.book_repository.DBConnection") as MockDBConnection:
      MockDBConnection.return_value.__enter__.return_value = mock_db

      response = book_repository.update(mock_book.id, mock_book)

    assert response == mock_book
    mock_session.query.return_value.filter.return_value.update.assert_called_once()
    mock_session.commit.assert_called_once()

  def test_rollback_and_raise_exception_when_book_not_found(self, book_repository: BookRepository, mock_book, mock_db_session):
    mock_db, mock_session = mock_db_session

    exception_message = f"Book with ID {mock_book.id} not found."
    mock_session.query.return_value.filter.return_value.update.return_value = 0

    with patch("repositories.book_repository.DBConnection") as MockDBConnection:
      MockDBConnection.return_value.__enter__.return_value = mock_db

      with pytest.raises(BookNotFoundException, match=exception_message):
        book_repository.update(mock_book.id, mock_book)

    mock_session.query.return_value.filter.return_value.update.assert_called_once()
    mock_session.commit.assert_not_called()
    mock_session.rollback.assert_called_once()

  def test_rollback_when_raise_exception(self, book_repository: BookRepository, mock_book, mock_db_session):
    mock_db, mock_session = mock_db_session

    mock_session.query.return_value.filter.return_value.update.side_effect = Exception("Error")

    with patch("repositories.book_repository.DBConnection") as MockDBConnection:
      MockDBConnection.return_value.__enter__.return_value = mock_db

      with pytest.raises(Exception, match="Error"):
        book_repository.update(mock_book.id, mock_book)

    mock_session.query.return_value.filter.return_value.update.assert_called_once()
    mock_session.commit.assert_not_called()
    mock_session.rollback.assert_called_once()