from src.application.celery.tasks import send_undone_todoes
from src.application.database import transaction
from src.infrastructure.database.schemas import User
from src.infrastructure.telegram import bot


@transaction
def start_handler(session, message):
    if not session.query(User).filter(User.chat_id == message.chat.id).first():
        session.add(User(chat_id=f"{message.chat.id}"))

    send_undone_todoes(chat_id=message.chat.id)
    bot.send_message(
        message.chat.id,
        f"Hello, {message.from_user.first_name} {message.from_user.last_name}!",
    )
