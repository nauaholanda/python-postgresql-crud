from repositories import BookRepository
from .fetch import fetch_books

def delete_book():
  fetch_books()

  try:
    id = int(input('\nEnter the ID of the book you want to delete: '))

    book_repository = BookRepository()
    book = book_repository.find_by_id(id)

    if not book: raise ValueError('Invalid ID entered')

    confirmation = input(f'Confirm deletion of the book "{book.title}" by {book.author} (ID {book.id})? (y/n) ')

    if confirmation.lower() == 'y':
      book_repository.delete(id)
      print('Book deleted successfully!')

  except Exception as err:
    print(f'Error deleting book: {err}. Returning to Menu...')