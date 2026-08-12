import os
import redis.asyncio as redis  # Ensure you are using the async client for FastAPI

# 1. Look for the Docker variable first, fallback to localhost only if running outside Docker
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")

# 2. Initialize the client using that URL
redis_client = redis.from_url(REDIS_URL, decode_responses=True)