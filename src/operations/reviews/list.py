from src.operations.books import fetch_books
from src.repositories import ReviewRepository

def list_reviews():
  fetch_books()

  try:
    book_id = int(input('\nEnter the ID of the book you want to list the reviews: '))

    review_repository = ReviewRepository()
    reviews = review_repository.find_all_by_book_id(book_id)

    for review in reviews:
      print(f"\nReviewer: {review.reviewer_name}\n{'-'*20}\n{review.review_text}")

  except Exception as err:
    print(f'Error listing reviews: {err}. Returning to Menu...')