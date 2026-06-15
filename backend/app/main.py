from fastapi import Fastapi

app = Fastapi()

@app.get("/")
def home():
    return {"message":"This is the base default page"}