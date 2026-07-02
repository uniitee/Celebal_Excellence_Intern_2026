from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

# from app import crud
from app.crud import question as question_crud, choice as choice_crud
from app.schemas.choice import ChoiceCreate, ChoiceOut
from app.dependencies import get_db

router = APIRouter(tags=["Choices"])


@router.post("/questions/{question_id}/choices", response_model=ChoiceOut, status_code=201)
def add_choice(question_id: int, choice: ChoiceCreate, db: Session = Depends(get_db)):
    question = question_crud.get_question(db, question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    return choice_crud.create_choice_for_question(db, question_id, choice)


@router.get("/questions/{question_id}/choices", response_model=list[ChoiceOut])
def list_choices(question_id: int, db: Session = Depends(get_db)):
    question = question_crud.get_question(db, question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    return choice_crud.get_choices_for_question(db, question_id)


@router.delete("/choices/{choice_id}", status_code=204)
def delete_choice(choice_id: int, db: Session = Depends(get_db)):
    deleted = choice_crud.delete_choice(db, choice_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Choice not found")
