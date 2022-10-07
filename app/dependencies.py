from app.db.repositories.rating_repository import RatingRepository
from app.db.database import SessionLocal

def get_rating_repository():
    with SessionLocal() as session:
        yield RatingRepository(session)