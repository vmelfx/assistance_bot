from src.application.celery.celeryconfig import app
from src.application.database import transaction
from src.infrastructure.database.schemas import Todoes, User
from src.infrastructure.models import TaskSubset
from src.infrastructure.telegram import bot


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(30.0, send_undone_todoes.s(), name='add every 10')


@app.task()
@transaction
def send_undone_todoes(session):
    # Get users with undone tasks
    users_with_undone_tasks = (
        session.query(User)
        .join(User.tasks)
        .filter(Todoes.complete.is_(False))
        .distinct()
        .all()
    )

    for user in users_with_undone_tasks:
        # Get undone tasks for the user
        tasks = [
            TaskSubset(
                task_id=task.task_id,
                description=task.task_description,
            )
            for task in user.tasks
        ]

        # Send notification to the user
        notification_message = "You have undone tasks. Here's your task list:\n"
        for task in tasks:
            notification_message += f"{task.task_id}. {task.description}\n"

        bot.send_message(user.chat_id, notification_message)
