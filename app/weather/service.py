import requests
from .models import WeatherData
from config import settings
from cache.redis_cache import RedisCache
import json
import httpx

class WeatherService:
    def __init__(self):
        self.redis_cache = RedisCache()

    async def initialize(self):
        await self.redis_cache.initialize()

    async def get_weather_by_city(self, city: str) -> WeatherData:
        if self.redis_cache is None:
            raise Exception("RedisCache is not initialized")

        # Verifica si el resultado está en el caché
        cached_weather = await self.redis_cache.get(city)
        if cached_weather:
            return WeatherData.from_json(json.loads(cached_weather))

        # Si no está en caché, obtén los datos de la API
        url = f"{settings.WEATHER_API_URL}/{city}"
        params = {
            'unitGroup': 'metric',
            'key': settings.API_KEY,
            'contentType': 'json'
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)

        if response.status_code != 200:
            raise Exception("Error fetching weather data")

        data = response.json()

        # Almacena los datos en el caché
        await self.redis_cache.set(city, json.dumps(data))

        return WeatherData.from_json(data)


