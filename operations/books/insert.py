from repositories import BookRepository
from entities import Book

def insert_book():
  try:
    title = input("Enter the title of the new book: ")
    if not title: raise ValueError('The book title is required!')
    author = input("Enter the author of this book: ")
    rating = float(input("Enter the rating for this book: "))

    book_repository = BookRepository()

    book_to_insert = Book(title=title, author=author, rating=rating)

    book_repository.insert(book_to_insert)

    print(f"Book '{title}' saved successfully!")

  except Exception as err:
    print(f'Error inserting book: {err}. Returning to Menu...')