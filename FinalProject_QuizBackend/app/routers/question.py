from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import question as question_crud
from app.schemas.question import QuestionCreate, QuestionOut
from app.dependencies import get_db

router = APIRouter(prefix="/questions", tags=["Questions"])


@router.post("/", response_model=QuestionOut, status_code=201)
def create_question(question: QuestionCreate, db: Session = Depends(get_db)):
    return question_crud.create_question(db, question)


@router.get("/", response_model=list[QuestionOut])
def list_questions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return question_crud.get_questions(db, skip=skip, limit=limit)


@router.get("/{question_id}", response_model=QuestionOut)
def get_question(question_id: int, db: Session = Depends(get_db)):
    db_question = question_crud.get_question(db, question_id)
    if not db_question:
        raise HTTPException(status_code=404, detail="Question not found")
    return db_question


@router.put("/{question_id}", response_model=QuestionOut)
def update_question(question_id: int, question: QuestionCreate, db: Session = Depends(get_db)):
    db_question = question_crud.update_question(db, question_id, question)
    if not db_question:
        raise HTTPException(status_code=404, detail="Question not found")
    return db_question


@router.delete("/{question_id}", status_code=204)
def delete_question(question_id: int, db: Session = Depends(get_db)):
    deleted = question_crud.delete_question(db, question_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Question not found")
