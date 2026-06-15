from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv


load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
database_url = os.getenv("DATABASE_URL")

engine = create_engine(database_url)
Sessionlocal = sessionmaker(autocommit=False,bind=engine)

Base = declarative_base()
def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()

