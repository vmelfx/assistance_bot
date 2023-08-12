import os
from contextlib import suppress
from importlib import import_module

from src.settings import SRC_FOLDER, TELEGRAM_BOT_API_KEY
from telebot import TeleBot


def create_bot():
    if not TELEGRAM_BOT_API_KEY:
        raise Exception("Telegram API key is not specified in the .env")

    return TeleBot(token=TELEGRAM_BOT_API_KEY)


def import_handlers():
    """
    Import all handlers files. It is a telebot infrastructure component
    """

    handlers_dir = SRC_FOLDER / "handlers"

    for app_name in os.listdir(handlers_dir):
        with suppress(ModuleNotFoundError, AttributeError):
            import_module(f"src.handlers.{app_name}")


# NOTE: The bot instance is created here since it is used for all handlers
bot: TeleBot = create_bot()
