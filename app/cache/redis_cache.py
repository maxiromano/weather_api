import redis
import os

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")

class RedisCache:
    def __init__(self):
        self.redis = None

    async def initialize(self):
        self.redis = redis.from_url(REDIS_URL, decode_responses=True)
        if self.redis is None:
            raise Exception("Failed to connect to Redis")

    async def get(self, key):
        if self.redis is None:
            raise Exception("RedisCache is not initialized")
        return self.redis.get(key)

    async def set(self, key, value, expire=43200):
        if self.redis is None:
            raise Exception("RedisCache is not initialized")
        await self.redis.set(key, value, expire=expire)



        
