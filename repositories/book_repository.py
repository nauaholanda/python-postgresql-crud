from configs import DBConnection
from entities import Book

class BookRepository:
  def select(self):
    with DBConnection() as db:
      books = db.session.query(Book).all()
      return books
    
  def insert(self, book):
    with DBConnection() as db:
      db.session.add(book)
      db.session.commit()