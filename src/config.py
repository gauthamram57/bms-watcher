from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

    MOVIE_NAME = os.getenv("MOVIE_NAME")
    VENUE_CODE = os.getenv("VENUE_CODE")
    REGION_CODE = os.getenv("REGION_CODE")
    DATE_CODE = os.getenv("DATE_CODE")

    CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", "300"))

