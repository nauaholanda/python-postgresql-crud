from entities import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey

class Review(Base):
  __tablename__ = 'reviews'
  
  id: Mapped[int] = mapped_column(primary_key=True)
  book_id: Mapped[int] = mapped_column(ForeignKey('books.id', ondelete='CASCADE'))
  review_text: Mapped[str] = mapped_column(nullable=False)
  reviewer_name: Mapped[str] = mapped_column(nullable=False)