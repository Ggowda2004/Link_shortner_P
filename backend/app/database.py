# from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base #sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
import os
from dotenv import load_dotenv


load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
database_url = os.getenv("DATABASE_URL")

# engine = create_engine(database_url)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

engine = create_async_engine(database_url, echo=False,pool_size=10, max_overflow=20)
#pool_size=10, max_overflow=20 means that the connection pool will maintain a maximum of 10 connections, and if all of those are in use, it can create up to 20 additional connections (for a total of 30) to handle bursts of traffic. Once the demand decreases, the extra connections will be closed.
AsyncSessionLocal = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)



Base = declarative_base()
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
        