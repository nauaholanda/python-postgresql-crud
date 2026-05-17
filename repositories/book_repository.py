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

  def find_by_id(self, id):
    with DBConnection() as db:
      book = db.session.query(Book).filter(Book.id == id).first()
      return book