import os
import redis.asyncio as redis  # Ensure you are using the async client for FastAPI

REDIS_URL = os.getenv("REDIS_URL")
if REDIS_URL:
    redis_client = redis.from_url(REDIS_URL, decode_responses=True)
else:
    redis_client = None
