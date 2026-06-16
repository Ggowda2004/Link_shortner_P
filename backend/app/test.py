import os
from dotenv import load_dotenv
from database import get_db
from sqlalchemy.orm import Session
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
print(os.getenv("DATABASE_URL"))

from contextlib import closing
from sqlalchemy import text

def test_db_connection():
    try:
        # closing() ensures next(get_db()) is properly terminated after use
        with closing(next(get_db())) as db:
            # text() is required for raw SQL string execution in SQLAlchemy 2.0+
            db.execute(text("SELECT 1"))
            print("Database connection successful!")
    except Exception as e:
        print(f"Database connection failed: {e}")