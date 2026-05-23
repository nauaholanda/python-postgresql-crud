from typing import Optional, List, TYPE_CHECKING
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import Float
from entities import Base

if TYPE_CHECKING:
  from entities import Review

class Book(Base):
  __tablename__ = 'books'
  
  id: Mapped[int] = mapped_column(primary_key=True)
  title: Mapped[str] = mapped_column(nullable=False)
  author: Mapped[str] = mapped_column(nullable=False)
  rating: Mapped[Optional[float]] = mapped_column(Float(precision=1))

  reviews: Mapped[List["Review"]] = relationship(back_populates='book')
  