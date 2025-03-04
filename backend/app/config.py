from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: str = os.getenv("DB_PORT")
    DB_NAME: str = os.getenv("DB_NAME")
    
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
    
    ALLOWED_WIFI_SSIDS: list = os.getenv("ALLOWED_WIFI_SSIDS").split(",")
    DEFAULT_GEOFENCE_RADIUS: float = float(os.getenv("DEFAULT_GEOFENCE_RADIUS"))

    class Config:
        env_file = ".env"

settings = Settings() 