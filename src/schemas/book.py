from pydantic import BaseModel

class BookResponse(BaseModel):
  id: int
  title: str
  author: str
  rating: float