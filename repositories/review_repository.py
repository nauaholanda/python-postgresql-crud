from configs import DBConnection
from entities import Review

class ReviewRepository:
  def find_all_by_book_id(book_id):
    with DBConnection() as db:
      book_reviews = db.session.query(Review).filter(Review.book_id == book_id).all()
      return book_reviews