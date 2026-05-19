from repositories import BookRepository
from entities import Book
from operations.books import fetch_books

def update_book():
  fetch_books()

  try:
    id = int(input('\nEnter the ID of the book you want to edit: '))

    book_repository = BookRepository()

    book = book_repository.find_by_id(id)

    title = input(f"Enter a new title for this book ({book.title}): ")
    if not title: title = book.title

    author = input(f"Enter a new author for this book ({book.author}): ")
    if not author: author = book.author

    rating_input = input(f"Enter a new rating for this book ({book.rating}): ")
    if not rating_input: rating = book.rating
    else: rating = float(rating_input)

    updated_book = Book(id=id, title=title, author=author, rating=rating)

    book_repository.update(updated_book)

    print('Book updated successfully!')

  except Exception as err:
    print(f'Error updating book: {err}. Returning to Menu...')