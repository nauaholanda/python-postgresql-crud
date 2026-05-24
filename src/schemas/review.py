from pydantic import BaseModel, ConfigDict

class ReviewResponse(BaseModel):
  model_config = ConfigDict(from_attributes=True) 

  id: int
  review_text: str
  reviewer_name: str
  book_id: int