from configs import DBConnection
from entities import Book
from exceptions import BookNotFoundException
from sqlalchemy.orm.exc import NoResultFound

class BookRepository:
  def select(self):
    with DBConnection() as db:
      books = db.session.query(Book).all()
      return books
    
  def insert(self, book):
    with DBConnection() as db:
      try:
        db.session.add(book)
        db.session.commit()
      except Exception as exception:
        db.session.rollback()
        raise exception

  def find_by_id(self, id):
    with DBConnection() as db:
      try:
        book = db.session.query(Book).filter(Book.id == id).one()
        return book
      except NoResultFound:
        return None
    
  def delete(self, id):
    with DBConnection() as db:
      try:
        db.session.query(Book).filter(Book.id == id).delete()
        db.session.commit()
      except Exception as exception:
        db.session.rollback()
        raise exception

  def update(self, book_id: int, update_data: dict) -> Book | None:
    with DBConnection() as db:
      try:
        rows_updated = db.session.query(Book).filter(Book.id == book_id).update(update_data)
        
        if rows_updated == 0:
            raise BookNotFoundException(f"Book with ID {book_id} not found.")
        
        db.session.commit()
        
        updated_book = db.session.query(Book).filter(Book.id == book_id).first()
        return updated_book
          
      except Exception as exception:
        db.session.rollback()
        raise exception