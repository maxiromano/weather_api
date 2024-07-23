from pydantic import BaseModel
from typing import Dict, Any

class CurrentConditions(BaseModel):
    temp: float
    humidity: float
    windspeed: float
    conditions: str

class WeatherData(BaseModel):
    city: str
    country: str
    current_conditions: CurrentConditions

    @classmethod
    def from_json(cls, data: Dict[str, Any]) -> 'WeatherData':
        return cls(
            city=data['resolvedAddress'],
            country=data.get('country', ''),
            current_conditions=CurrentConditions(
                temp=data['currentConditions']['temp'],
                humidity=data['currentConditions']['humidity'],
                windspeed=data['currentConditions']['windspeed'],
                conditions=data['currentConditions']['conditions']
            )
        )
