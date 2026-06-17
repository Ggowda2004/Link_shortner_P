from typing import List
from fastapi import APIRouter, Depends, HTTPException
from services import create_url, get_all_urls, get_url_by_code
from schemas import UrlCreate, UrlResponse
from database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    tags=["url-short"]
)


@router.post(
    "/shorten",
    summary="Shorten the url",
    response_description="new shortned url")
def shorten_url(url:UrlCreate, db: Session = Depends(get_db)):
    try:
        new_url = create_url(url, db )
        return new_url
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
    response_description="to the original ur")
def redirect_url(short_code:str,db: Session = Depends(get_db)):
    return get_url_by_code(short_code,db)



# POST /shorten *
# GET /{short_code}
# GET /urls