import requests
from celery import Celery
from src.application.celery import tasks
from src.settings import TELEGRAM_BOT_API_KEY

app = Celery("vmelfx_assistant_bot")

app.conf.beat_schedule = {
    "periodic-task": {
        "task": "send_todo",  # Path to your periodic task function
        "schedule": 30,  # Every hour (in seconds)
    },
}


# @app.task(name="send_todo")
# def send_undone_todoes():
#     chat_id = 286047739
#     message = "test periodic task"
#     url = f"https://api.telegram.org/bot{TELEGRAM_BOT_API_KEY}/sendMessage"
#     params = {"chat_id": chat_id, "text": message}
#     response = requests.post(url, params=params)
#     return response.json()
