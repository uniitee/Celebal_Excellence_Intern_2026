from typing import List
from pydantic import BaseModel, ConfigDict, Field, model_validator
from app.schemas.choice import ChoiceCreate, ChoiceOut


class QuestionBase(BaseModel):
    question_text: str = Field(
        min_length=4,
        max_length=300
    )


class QuestionCreate(QuestionBase):
    # Lets a client POST a question and its choices in a single request.
    choices: List[ChoiceCreate]
    category: str | None = None

    @model_validator(mode="after")
    def validate_choices(self):
        correct = sum(choice.is_correct for choice in self.choices)
        if correct < 1:
            raise ValueError("There Should Be AtLeast 1 choice marked correct ^_^")
        return self


class QuestionOut(QuestionBase):
    id: int
    question_text:str
    category: str | None
    # choices: List[ChoiceOut] = []
    choices: List[ChoiceOut] = Field(default_factory=list)
    model_config = ConfigDict(from_attributes=True)
