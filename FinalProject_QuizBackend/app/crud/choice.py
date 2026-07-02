from sqlalchemy.orm import Session

from app.models.choice import Choice
from app.schemas.choice import ChoiceCreate


def create_choice_for_question(db: Session, question_id: int, choice: ChoiceCreate) -> Choice:
    db_choice = Choice(**choice.model_dump(), question_id=question_id)
    db.add(db_choice)
    db.commit()
    db.refresh(db_choice)
    return db_choice


def get_choices_for_question(db: Session, question_id: int) -> list[Choice]:
    return db.query(Choice).filter(Choice.question_id == question_id).all()


def delete_choice(db: Session, choice_id: int) -> bool:
    db_choice = db.query(Choice).filter(Choice.id == choice_id).first()
    if not db_choice:
        return False
    db.delete(db_choice)
    db.commit()
    return True
