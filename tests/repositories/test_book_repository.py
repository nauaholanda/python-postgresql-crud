import pytest

from src.repositories.book_repository import BookRepository

@pytest.fixture
def book_repository():
  return BookRepository()