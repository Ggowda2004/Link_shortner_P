from fastapi import FastAPI
from routes.urls import router as url_router
from database import engine, Base
import models

app = FastAPI()
# Create tables
models.Base.metadata.create_all(bind=engine)

app.include_router(url_router)

@app.get("/")
def home():
    return {"message":"This is the base default page"}