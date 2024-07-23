from fastapi import APIRouter, HTTPException
from weather.service import WeatherService
from weather.schemas import WeatherDataSchema
from weather.models import WeatherData

router = APIRouter()

@router.get("/weather/{city}", response_model=WeatherDataSchema)
async def get_weather_by_city(city: str):
    weather_service = WeatherService()
    try:
        await weather_service.initialize()
        weather_data = await weather_service.get_weather_by_city(city)
        return weather_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))