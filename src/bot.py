from os import getenv

import telebot  # type: ignore
from application.database import transaction
from infrastructure.database.schemas import Todoes, User, create_db

bot = telebot.TeleBot(getenv("TELEBOT_API_KEY", default=""))
create_db()


@bot.message_handler(commands=["start"])
@transaction
def start_handler(session, message):
    if not session.query(User).filter(User.chat_id == message.chat.id).first():
        session.add(User(chat_id=f"{message.chat.id}"))

    bot.send_message(
        message.chat.id,
        f"Hello, {message.from_user.first_name} {message.from_user.last_name}!",
    )


@bot.message_handler(content_types=["text"])
@transaction
def create_todo_handler(session, message):
    user = session.query(User).filter(User.chat_id == message.chat.id).first()
    session.add(
        Todoes(
            user=user,
            description=message.text,
        )
    )
    bot.send_message(message.chat.id, "Your todo was saved")


bot.infinity_polling()
