from schemas import UrlCreate, UrlResponse
import secrets, string
from sqlalchemy.orm import Session
from models import urls
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, Depends
from starlette.responses import RedirectResponse
from redis_client import redis_client
import time


#code_generation
def generate_code(length=6):
    chars = string.ascii_letters + string.digits  # 62 characters
    return "".join((secrets.choice(chars)) for _ in range(length))

def create_url(url:UrlCreate, db: Session):
    try_n = 0
    while try_n<=5:
        short_code = generate_code()
        new_url = urls(
            original_url = str(url.original_url),
            short_code = short_code,   
        )
        db.add(new_url)
        try:
            db.commit()
            db.refresh(new_url)
            return new_url
        except IntegrityError:
            db.rollback()
        try_n+=1
    raise HTTPException(status_code=500, detail="Could not generate unique short code")


def increment_click_count(db:Session, url:urls)->None:
    url.click_count += 1
    db.commit()
    db.refresh(url)
    

def get_url_by_code(short_code:str,db: Session):
    start_time = time.perf_counter()
    cached_url = redis_client.get(short_code)

    if cached_url:
        redis_time = (time.perf_counter() - start_time) * 1000
        print(f"Cache hit. Time taken: {redis_time:.2f} ms")
        increment_click_count(db, db.query(urls).filter(urls.short_code==short_code).first())
        return RedirectResponse(url = cached_url)
    
    url = db.query(urls).filter(urls.short_code==short_code).first()
    if not url:
        raise HTTPException(status_code=404, detail="URL not found")
    # url.click_count+=1
    # db.commit()
    # db.refresh(url)
    increment_click_count(db, url)
    redis_client.set(short_code, url.original_url, ex=3600)  # Cache for 1 hour
    db_time = (time.perf_counter() - start_time) * 1000  # Convert to milliseconds
    print(f"⏳ Cache miss! DB Fetch Time taken: {db_time:.4f} ms")
    return RedirectResponse(url=url.original_url)

def get_all_urls(db: Session):
    # all_urls = db.query(urls).all()
    # if not all_urls:
    #     return []
    # return all_urls
    return db.query(urls).all()



# Depends() belongs in FastAPI route functions, not CRUD functions.and inject the dependency in the route: