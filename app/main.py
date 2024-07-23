from fastapi import FastAPI
from api import endpoints
from cache.redis_cache import RedisCache
from contextlib import asynccontextmanager

redis_cache = RedisCache()

@asynccontextmanager
async def app_lifespan(app: FastAPI):
    # Evento de inicio
    print("Initializing Redis cache...")
    await redis_cache.initialize()
    print("Redis cache initialized.")
    
    # Mantener la aplicación viva
    yield

app = FastAPI(lifespan=app_lifespan)

app.include_router(endpoints.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)



