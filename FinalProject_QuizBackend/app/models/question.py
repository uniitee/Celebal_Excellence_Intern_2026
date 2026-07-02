from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(String, nullable=False)
    category = Column(String, nullable=True) # why was the resource added so late ^_^ ?

    # One question -> many choices. cascade delete -> ! orphan choices
    choices = relationship(
        "Choice",
        back_populates="question",
        cascade="all, delete-orphan",
    )
