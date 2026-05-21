from src.repositories import BookRepository

def fetch_books():
  book_repository = BookRepository()

  books = book_repository.select()

  print(f'We have {len(books)} books registered in our database:')

  for book in books:
    print(f'{book.id} - {book.title} by {book.author} - Rating: {book.rating}/10.0')