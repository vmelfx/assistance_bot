from src.application.database import transaction
from src.infrastructure.database.schemas import Todoes
from src.infrastructure.telegram import bot


# @bot.message_handler(regexp=r"\d+ done")
@transaction
def mark_as_done(session, message):
    received_task_id = message.text.split(" ")[0]
    task = session.query(Todoes).filter(Todoes.task_id == received_task_id).first()
    task.complete = True
    bot.send_message(
        message.chat.id,
        f"{task.task_id} marked as done",
    )
