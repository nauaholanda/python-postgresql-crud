from typing import Optional
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Float
from entities import Base

class Book(Base):
  __tablename__ = 'books'
  
  id: Mapped[int] = mapped_column(primary_key=True)
  title: Mapped[str] = mapped_column(nullable=False)
  author: Mapped[str] = mapped_column(nullable=False)
  review_points: Mapped[Optional[float]] = mapped_column(Float(precision=1))
  