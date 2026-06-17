from pydantic import BaseModel
import uuid
from datetime import datetime

class UrlCreate(BaseModel):
    original_url : str

class UrlResponse(BaseModel):
    id :uuid.UUID
    original_url:str
    short_code:str
    click_count : int
    created_at:datetime

    class Config:
        orm_mode = True
    #Pydantic will look at the object’s attributes (like url.id, url.original_url) instead of expecting a dict.
