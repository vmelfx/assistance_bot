from os import getenv
from pathlib import Path

SRC_FOLDER = Path(__file__).parent
ROOT_FOLDER = SRC_FOLDER.parent

DATABASE_NAME = getenv("DATABASE_NAME", default="db")
DATABASE_URL = f"sqlite:///{ROOT_FOLDER}/{DATABASE_NAME}"


# Telegram-related configurations
TELEGRAM_BOT_API_KEY: str | None = getenv("TELEGRAM_BOT_API_KEY")
