from datetime import date

from src.application.database import transaction
from src.infrastructure.database.schemas import Todoes, User
from src.infrastructure.telegram import bot


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
