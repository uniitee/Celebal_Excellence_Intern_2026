from app.database import SessionLocal

def get_db():
    """Yields a DB session per request and always closes it afterward."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()