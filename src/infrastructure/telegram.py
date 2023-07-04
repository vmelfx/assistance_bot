from src.settings import TELEGRAM_BOT_API_KEY
from telebot import TeleBot


def create_bot():
    if not TELEGRAM_BOT_API_KEY:
        raise Exception("Telegram API key is not specified in the .env")

    return TeleBot(token=TELEGRAM_BOT_API_KEY)


# NOTE: The bot instance is created here since it is used for all handlers
bot: TeleBot = create_bot()
