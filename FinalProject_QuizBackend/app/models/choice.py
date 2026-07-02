from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Choice(Base):
    __tablename__ = "choices"

    id = Column(Integer, primary_key=True, index=True)
    choice_text = Column(String, nullable=False)
    is_correct = Column(Boolean, default=False, nullable=False)
    question_id = Column(Integer, ForeignKey("questions.id"), nullable=False)

    question = relationship("Question", back_populates="choices")
