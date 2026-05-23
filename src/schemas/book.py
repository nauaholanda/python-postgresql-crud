from typing import Optional

from pydantic import BaseModel, ConfigDict

class BookResponse(BaseModel):
  model_config = ConfigDict(from_attributes=True) 

  id: int
  title: str
  author: str
  rating: float

class BookCreate(BaseModel):
  title: str
  author: str
  rating: float

class BookUpdate(BaseModel):
  title: Optional[str] = None
  author: Optional[str] = None
  rating: Optional[float] = None