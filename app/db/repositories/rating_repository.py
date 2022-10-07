from typing import List
from datetime import datetime
from sqlalchemy.orm import Session
from app.db.models.rating import RatingModel
from app.schemas.rating import RatingScale

class RatingRepository():

    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_rating(self, scale: RatingScale, original_text: str, translated_text: str, translation_model_version: str, submitted_date: datetime):
        new_rating = RatingModel(
            scale = scale, 
            original_text = original_text, 
            translated_text = translated_text, 
            translation_model_version = translation_model_version, 
            submitted_date = submitted_date
        )
        self.db_session.add(new_rating)
        return self.db_session.commit()


    """ 
    It would be better to introduce paging here, not fetching all records at once, for performance reasons, 
    but should be enough for a demo purposes, to test out the retrieval of the ratings
    """ 
    def get_ratings(self) -> List[RatingModel]:
        # .offset(m).limit(n).all():
        return self.db_session.query(RatingModel).all()