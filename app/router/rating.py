from typing import List
from datetime import datetime, timezone
from fastapi import APIRouter, status, Depends
from app.schemas import rating
from app.db.repositories.rating_repository import RatingRepository
from app.dependencies import get_rating_repository
from app.translation_model import get_model_version

router = APIRouter(
  prefix='/rating',
  tags=['rating']
)

@router.get('/', response_model=List[rating.Rating])
def get_ratings(ratingRepo: RatingRepository = Depends(get_rating_repository)):
  return ratingRepo.get_ratings()

@router.post('/', status_code=status.HTTP_204_NO_CONTENT)
def create_rating(request: rating.CreateRating, ratingRepo: RatingRepository = Depends(get_rating_repository)):
  translation_model_version = get_model_version(request.source_language, request.target_language)
  ratingRepo.create_rating(request.scale, request.original_text, request.translated_text, translation_model_version, datetime.now(timezone.utc))
  pass