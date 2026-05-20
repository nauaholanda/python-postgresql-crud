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
      book = db.session.query(Book).filter(Book.id == id).one()
      return book
    
  def delete(self, id):
    with DBConnection() as db:
      db.session.query(Book).filter(Book.id == id).delete()
      db.session.commit()

  def update(self, book: Book):
    with DBConnection() as db:
      db.session.query(Book).filter(Book.id == book.id).update({
        'title': book.title,
        'author': book.author,
        'rating': book.rating
      })
      db.session.commit()