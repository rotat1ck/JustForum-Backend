from typing import Final
from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    PORT: Final[int] = os.getenv("PORT") or 5000
    DEBUG: Final[bool] = os.getenv("DEBUG") or False
    APP_URL: Final[str] = os.getenv("APP_URL") or "127.0.0.1"
    DATABASE: Final[str] =os.getenv("DATABASE") or "database/database.db"