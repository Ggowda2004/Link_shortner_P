# from redis import Redis

# redis_client = Redis(
#     host="localhost",
#     port=6379,
#     decode_responses=True
# )



import redis.asyncio as aioredis

redis_client = aioredis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

async def get_redis():
    yield redis_client

# sudo service redis-server start