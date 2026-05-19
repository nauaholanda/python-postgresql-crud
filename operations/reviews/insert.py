from operations.books import fetch_books
from entities import Review
from repositories import ReviewRepository

def insert_review():
  fetch_books()

  try:
    book_id = int(input('\nEnter the ID of the book you want to insert a review: '))

    reviewer_name = input('Enter the reviewer name: ')
    if not reviewer_name: raise ValueError('The reviewer name is required!')
    review_text = input('Enter the review text: ')
    if not review_text: raise ValueError('The reviewer text is required!')

    review = Review(reviewer_name=reviewer_name, review_text=review_text, book_id=book_id)

    review_repository = ReviewRepository()
    review_repository.insert(review)

    print("Review inserted successfully!")

  except Exception as err:
    print(f'Error inserting review: {err}. Returning to Menu...')