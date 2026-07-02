from pydantic import BaseModel


class ChoiceBase(BaseModel):
    choice_text: str
    is_correct: bool = False


class ChoiceCreate(ChoiceBase):
    """Shape expected when creating a choice (nested inside a question). :)"""
    pass


class ChoiceOut(ChoiceBase):
    id: int
    question_id: int

    class Config:
        from_attributes = True  # lets Pydantic read SQLAlchemy objects directly
