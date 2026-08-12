from fastapi import FastAPI
from routes.urls import router as url_router
from database import engine, Base
import models
from fastapi.middleware.cors import CORSMiddleware
from redis_client import redis_client
from contextlib import asynccontextmanager
from fastapi import FastAPI

#async def create_tables():
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Database connection active. Generating tables...")
    await create_tables()
    # Startup logic
    yield
    # Shutdown logic
    await redis_client.aclose()

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)
# Create tables
# models.Base.metadata.create_all(bind=engine)


#running it at startup
app.include_router(url_router)

@app.get("/")
def home():
    return {"message":"This is the base default page"}