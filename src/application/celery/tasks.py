from src.application.celery.celeryconfig import app
from src.application.database import transaction
from src.infrastructure.database.schemas import Todoes, User
from src.infrastructure.models import TaskSubset
from src.infrastructure.telegram import bot


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    """Periodic task options such as time, name etc should be configured here"""

    sender.add_periodic_task(30.0, send_undone_todoes.s(), name='add every 10')
    sender.add_periodic_task(
        30.0,
        send_daily_notification_to_users.s(),
        name="send_daily_notification_to_user",
    )


@app.task()
@transaction
def send_undone_todoes(session):
    """
    This task is used to send to users notifications about undone tasks
    """

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
        undone_tasks = [
            TaskSubset(
                task_id=task.task_id,
                description=task.task_description,
            )
            for task in user.tasks
            if not task.complete
        ]

        # Send notification to the user
        notification_message = "You have undone tasks. Here's your task list:\n"
        for task in undone_tasks:
            notification_message += f"{task.task_id}. {task.description}\n"

        bot.send_message(user.chat_id, notification_message)


@app.task()
@transaction
def send_daily_notification_to_users(session):
    """
    This task is used to send to users notification about the absence of undone tasks
    """

    # Subquery to get get user's chat_id with undone tasks and then exlude them from the main query
    users_without_undone_tasks_subquery = (
        session.query(User.chat_id)
        .join(User.tasks)
        .filter(Todoes.complete.is_(False))
        .distinct()
        .subquery()
    )

    users_without_undone_tasks = (
        session.query(User)
        .filter(User.chat_id.notin_(users_without_undone_tasks_subquery))
        .all()
    )

    notification_message = "You don't have any undone tasks! Congrats!"

    for user in users_without_undone_tasks:
        bot.send_message(user.chat_id, notification_message)
