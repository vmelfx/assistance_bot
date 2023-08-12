"""
The application entrypoint.

NOTE: All handlers should be imported here due to the telebot requirement
"""

from src.handlers import *  # noqa: F401, F403
from src.infrastructure.telegram import bot


def start_bot_loop():
    while True:
        try:
            bot.polling(none_stop=True, interval=0)
        except Exception as err:
            print(err, "Bot is down. \nRestarting")


start_bot_loop()
