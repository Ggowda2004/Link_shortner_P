from typing import List
from fastapi import APIRouter, Depends, HTTPException
from services import create_url, get_all_urls, get_url_by_code
from schemas import UrlCreate, UrlResponse
from database import get_db
# from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from dependencies import RateLimiter

router = APIRouter(
    tags=["url-short"]
)


@router.post(
    "/shorten",
    summary="Shorten the url",
    # response_model=UrlResponse,
    response_description="new shortned url",
    dependencies=[Depends(RateLimiter(10, route_name="shorten"))])
async def shorten_url(url:UrlCreate, db: AsyncSession = Depends(get_db)):
    try:
        new_url = await create_url(url, db )
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
async def list_urls(db: AsyncSession = Depends(get_db)):
    urls = await get_all_urls(db)
    return urls

@router.get("/{short_code}",
    summary="redirecting to the original url",
    response_description="to the original ur",
    dependencies=[Depends(RateLimiter(100,route_name="redirect"))])
async def redirect_url(short_code:str,db: AsyncSession = Depends(get_db)):
    return await get_url_by_code(short_code,db)



# POST /shorten *
# GET /{short_code}
# GET /urls
#🔒 Limit to 100 requests per minute per IP for get and 10 for post