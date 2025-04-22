from typing import Final
from dotenv import load_dotenv
from os import getenv, path

load_dotenv()

class Config:
    PORT: Final[int] = getenv("PORT") or 4999
    DEBUG: Final[bool] = getenv("DEBUG") or False
    APP_URL: Final[str] = getenv("APP_URL") or "127.0.0.1"
    DATABASE: Final[str] = getenv("DATABASE") or "database/database.db"