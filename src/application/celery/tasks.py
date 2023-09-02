import requests
from src.application.celery.celeryconfig import app
from src.settings import TELEGRAM_BOT_API_KEY

app.conf.beat_schedule = {
    "periodic-task": {
        "task": "send_todo",
        "schedule": 30,
    },
}


@app.task(name="send_todo")
def send_undone_todoes():
    chat_id = 286047739
    message = "test periodic task"
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_API_KEY}/sendMessage"
    params = {"chat_id": chat_id, "text": message}
    response = requests.post(url, params=params)
    return response.json()
