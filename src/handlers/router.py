from src.handlers import start_handler


def message_router(message):
    if message.text.startswith("/start"):
        start_handler(message)
