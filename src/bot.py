from os import getenv

import telebot  # type: ignore
from database.database import SessionLocal, create_db
from database.schemas import Todoes, User

bot = telebot.TeleBot(getenv("TELEBOT_API_KEY", default=""))
create_db()


@bot.message_handler(commands=["start"])
def start_handler(message):
    with SessionLocal() as session:
        try:
            if not session.query(User).filter(User.chat_id == message.chat.id).first():
                session.add(User(chat_id=f"{message.chat.id}"))
        except Exception:
            session.rollback()
            raise
        else:
            session.commit()
    bot.send_message(
        message.chat.id,
        f"Hello, {message.from_user.first_name} {message.from_user.last_name}!",
    )


@bot.message_handler(content_types=["text"])
def create_todo_handler(message):
    with SessionLocal() as session:
        user = session.query(User).filter(User.chat_id == message.chat.id).first()
        try:
            session.add(
                Todoes(
                    user=user,
                    description=message.text,
                )
            )
        except Exception:
            session.rollback()
            raise
        else:
            session.commit()
        bot.send_message(message.chat.id, "Your todo was saved")


bot.infinity_polling()
