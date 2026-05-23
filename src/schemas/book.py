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