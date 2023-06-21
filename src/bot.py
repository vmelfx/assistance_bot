from os import getenv

import telebot  # type: ignore
from database.database import SessionLocal, create_db
from database.schemas import Todoes, User

bot = telebot.TeleBot(getenv("TELEBOT_API_KEY", default=""))
create_db()


def session_scope(func):
    session = SessionLocal()

    def wrapper(*args, **kwargs):
        try:
            result = func(session, *args, **kwargs)
            session.commit()
            return result
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    return wrapper


@bot.message_handler(commands=["start"])
@session_scope
def start_handler(session, message):
    user = User(chat_id=f"{message.chat.id}")
    session.add(user)
    bot.send_message(
        message.chat.id,
        f"Hello, {message.from_user.first_name} {message.from_user.last_name}!",
    )


@bot.message_handler(content_types=["text"])
def create_todo_handler(message):
    pass


bot.infinity_polling()
