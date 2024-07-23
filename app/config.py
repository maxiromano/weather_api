import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

class Settings():
    API_KEY: str = os.getenv("API_KEY")
    WEATHER_API_URL: str = os.getenv('WEATHER_API_URL')

settings = Settings()