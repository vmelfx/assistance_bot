from datetime import date

from src.application.database import transaction
from src.infrastructure.database.schemas import Todoes, User
from src.infrastructure.telegram import bot


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
        if todo.complete:
            formatted_message.append(
                f"<b><s>{todo.task_id}. {todo.task_description}</s></b>\n"
            )
        else:
            formatted_message.append(f"<b>{todo.task_id}. {todo.task_description}</b>\n")

    if formatted_message:
        bot.send_message(
            message.chat.id,
            "".join(formatted_message),
            parse_mode="HTML",
        )
    else:
        bot.send_message(
            message.chat.id,
            "There is no tasks for today.",
            parse_mode="HTML",
        )
