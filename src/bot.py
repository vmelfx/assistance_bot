from datetime import date

from src.application.database import transaction
from src.infrastructure.database.schemas import Todoes, User
from src.infrastructure.telegram import bot


@bot.message_handler(commands=["start"])
@transaction
def start_handler(session, message):
    if not session.query(User).filter(User.chat_id == message.chat.id).first():
        session.add(User(chat_id=f"{message.chat.id}"))

    bot.send_message(
        message.chat.id,
        f"Hello, {message.from_user.first_name} {message.from_user.last_name}!",
    )


@bot.message_handler(commands=["today", "t"])
@transaction
def get_todo_list_on_today(session, message):
    user = session.query(User).filter(User.chat_id == message.chat.id).first()
    todoes = (
        session.query(Todoes)
        .filter(
            Todoes.user == user,
            Todoes.date == date.today(),
        )
        .all()
    )

    formatted_message = []
    for todo in todoes:
        formatted_message.append(f"<b>{todo.task_description}</b>\n")

    bot.send_message(
        message.chat.id,
        "".join(formatted_message),
        parse_mode="HTML",
    )


@bot.message_handler(content_types=["text"])
@transaction
def create_todo_handler(session, message):
    user = session.query(User).filter(User.chat_id == message.chat.id).first()
    session.add(
        Todoes(
            user=user,
            task_description=message.text,
            date=date.today(),
        )
    )

    bot.send_message(message.chat.id, "Your todo was saved")


bot.infinity_polling()
