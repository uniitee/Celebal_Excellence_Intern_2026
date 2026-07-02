from fastapi import FastAPI

from app.database import Base, engine
from app import models 
from app.routers import question, choice
# import asyncio
# import uuid

# Creates tables if they don't exist yet
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Quiz Backend Management System",
    description="A RESTful API to manage quiz questions and choices.",
    version="1.0.0",
)

app.include_router(question.router)
app.include_router(choice.router)


@app.get("/")
def root():
    return {"message": "Quiz Backend is running. Visit /docs for the interactive API."}