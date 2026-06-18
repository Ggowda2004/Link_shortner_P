from typing import List
from fastapi import APIRouter, Depends, HTTPException
from services import create_url, get_all_urls, get_url_by_code
from schemas import UrlCreate, UrlResponse
from database import get_db
from sqlalchemy.orm import Session
from dependencies import RateLimitter

router = APIRouter(
    tags=["url-short"]
)


@router.post(
    "/shorten",
    summary="Shorten the url",
    # response_model=UrlResponse,
    response_description="new shortned url",
    dependencies=[Depends(RateLimitter(10,route_name="shorten"))])
def shorten_url(url:UrlCreate, db: Session = Depends(get_db)):
    try:
        new_url = create_url(url, db )
        # create_url returns the ORM object; frontend expects a `short_url` string
        return {"short_url": f"http://localhost:8000/{new_url.short_code}"}
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Failed to shorten the url: {str(e)}"
        )

@router.get("/all_urls",
            summary="get all urls",
            response_description="list of all urls",
            response_model=List[UrlResponse])
def list_urls(db: Session = Depends(get_db)):
    urls = get_all_urls(db)
    return urls

@router.get("/{short_code}",
    summary="redirecting to the original url",
    response_description="to the original ur",
    dependencies=[Depends(RateLimitter(100,route_name="redirect"))])
def redirect_url(short_code:str,db: Session = Depends(get_db)):
    return get_url_by_code(short_code,db)



# POST /shorten *
# GET /{short_code}
# GET /urls
#🔒 Limit to 100 requests per minute per IP for get and 10 for post