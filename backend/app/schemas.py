from pydantic import BaseModel, ConfigDict, AnyHttpUrl
import uuid
from datetime import datetime

class UrlCreate(BaseModel):
    original_url: AnyHttpUrl

class UrlResponse(BaseModel):
    id :uuid.UUID
    original_url:str
    short_code:str
    click_count : int
    created_at:datetime

    # class Config:
    #     # orm_mode = True
    #     from_attributes = True
        #i updated to pydantic v2, so instead of orm_mode, we use from_attributes. This allows Pydantic to read data from ORM objects directly, without needing to convert them to dicts first.
    #Pydantic will look at the object’s attributes (like url.id, url.original_url) instead of expecting a dict.

     # 2. Define it as a direct class variable using ConfigDict
    model_config = ConfigDict(from_attributes=True)
