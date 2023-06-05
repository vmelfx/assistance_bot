from os import getenv

import telebot

bot = telebot.TeleBot(getenv("TELEBOT_API_KEY", default=""))


@bot.message_handler(commands=["start"])
def start_handler(message):
    bot.send_message(
        message.chat.id,
        f"Hello, {message.from_user.first_name} {message.from_user.last_name}!",
    )


bot.infinity_polling()
