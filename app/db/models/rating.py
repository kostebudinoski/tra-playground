from sqlalchemy import Enum
from sqlalchemy.sql.sqltypes import Integer, String, DateTime
from app.db.database import Base
from sqlalchemy import Column

from app.schemas.rating import RatingScale


class RatingModel(Base):
  __tablename__ = 'ratings'

  id = Column(Integer, primary_key=True, index=True)
  scale = Column(Enum(RatingScale))
  original_text = Column(String)
  translated_text = Column(String)
  translation_model_version = Column(String)
  submitted_date = Column(DateTime)  
