from typing import TYPE_CHECKING
from entities import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey

if TYPE_CHECKING:
  from entities import Book

class Review(Base):
  __tablename__ = 'reviews'
  
  id: Mapped[int] = mapped_column(primary_key=True)
  book_id: Mapped[int] = mapped_column(ForeignKey('books.id', ondelete='CASCADE'))
  review_text: Mapped[str] = mapped_column(nullable=False)
  reviewer_name: Mapped[str] = mapped_column(nullable=False)

  book: Mapped["Book"] = relationship(back_populates='reviews')