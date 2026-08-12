import datetime
from fastapi import Request, HTTPException, status
from redis_client import redis_client


class RateLimiter:
    def __init__(self, limit:int, route_name:str):
        self.limit = limit
        self.route_name = route_name
    
    async def __call__(self, request:Request):
        if redis_client is None:
            return

        client_ip = request.client.host if request.client else "unknown"
        current_minute = datetime.datetime.utcnow().strftime("%Y-%m-%d-%H%M")
        redis_key = f"rate:{self.route_name}:{client_ip}:{current_minute}"

        current_requests = await redis_client.incr(redis_key)
        if current_requests == 1:
            await redis_client.expire(redis_key, 60)

        if current_requests > self.limit:
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail="Too many requests. Please try again in the next minute."
            )
