from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field

class RatingScale(str, Enum):
    UNACCEPTABLE = "UNACCEPTABLE"
    WEAK = "WEAK"
    GOOD = "GOOD"
    VERYGOOD = "VERYGOOD"
    EXCELLENT = "EXCELLENT"

class RatingBase(BaseModel):
  scale: RatingScale = Field(default=..., title="The rating of the translation")
  original_text: str = Field(default=..., title="The original text of the translation")
  translated_text: str = Field(default=..., title="The translate text of the translation")

class Rating(RatingBase):
  id: int
  submitted_date: datetime
  translation_model_version: str

  class Config():
    orm_mode = True

class CreateRating(RatingBase):
  source_language: str = Field(default=..., title="The source language of the translation")
  target_language: str = Field(default=..., title="The target language of the translation")