# Quiz Backend Management System

A RESTful API built with FastAPI to manage quiz questions and choices.
Uses SQLAlchemy for the ORM/database layer and Pydantic for request/response validation.

## Setup

```bash
# Clone the repository
git clone repo_url
cd FinalProject_QuizBackend

# Setup virtual environment
uv venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# install dependencies
uv add fastapi sqlalchemy uvicorn
```

## Run

```bash
# Run the server
uv run python -m uvicorn app.main:app --reload
```




## Endpoints

| Method | Path | Description |
|---|---|---|
| POST | `/questions/` | Create a question with nested choices |
| GET | `/questions/` | List all questions |
| GET | `/questions/{id}` | Get one question |
| PUT | `/questions/{id}` | Update a question and replace its choices |
| DELETE | `/questions/{id}` | Delete a question (cascades to its choices) |
| POST | `/questions/{id}/choices` | Add a single choice to an existing question |
| GET | `/questions/{id}/choices` | List choices for a question |
| DELETE | `/choices/{id}` | Delete a single choice |

## Example request

```json
POST /questions/
{
  "question_text": "What is Python?",
  "category": "Programming",
  "choices": [
    { "choice_text": "Language", "is_correct": true },
    { "choice_text": "Snake", "is_correct": false },
    { "choice_text": "Easy", "is_correct": true }
  ]
}
```

## Demo Walkthrough
<!-- video display -->
![Quiz Backend Demo](./public/quiz_backend.gif)


Made with <3 by [@UniiTee](https://github.com/uniitee)