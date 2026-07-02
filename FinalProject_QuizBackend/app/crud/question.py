from sqlalchemy.orm import Session

from app.models.question import Question
from app.models.choice import Choice
from app.schemas.question import QuestionCreate


def create_question(db: Session, question: QuestionCreate) -> Question:
    db_question = Question(
        question_text=question.question_text, # SQLAlchemy obj init
        category = question.category
    )
    db.add(db_question) # still not in db and !id
    db.flush()  # gets db_question.id before commit -> choices can reference it

    for choice in question.choices:
        db.add(Choice(**choice.model_dump(), question_id=db_question.id)) # ** -> dictionary unpacking

    db.commit() # stored in db
    db.refresh(db_question)
    return db_question


def get_question(db: Session, question_id: int) -> Question | None:
    return db.query(Question).filter(Question.id == question_id).first()


def get_questions(db: Session, skip: int = 0, limit: int = 100) -> list[Question]:
    return db.query(Question).offset(skip).limit(limit).all()


def update_question(db: Session, question_id: int, question: QuestionCreate) -> Question | None:
    db_question = get_question(db, question_id)
    if not db_question:
        return None

    db_question.question_text = question.question_text
    db_question.category = question.category

    # replace strategy, all choices :)
    db_question.choices.clear()
    for choice in question.choices:
        db.add(Choice(**choice.model_dump(), question_id=db_question.id))

    db.commit()
    db.refresh(db_question)
    return db_question


def delete_question(db: Session, question_id: int) -> bool:
    db_question = get_question(db, question_id)
    if not db_question:
        return False
    db.delete(db_question)  # cascades to choices ->(!orphan records)
    db.commit()
    return True
