from pydantic import BaseModel

class CurrentConditionsSchema(BaseModel):
    temp: float
    humidity: float
    windspeed: float
    conditions: str

class WeatherDataSchema(BaseModel):
    city: str
    country: str
    current_conditions: CurrentConditionsSchema
