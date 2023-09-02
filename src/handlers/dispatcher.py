from src.handlers.create_todo import create_todo_handler
from src.handlers.get_todo_list_on_today import get_todo_list_on_today
from src.handlers.mark_as_done import mark_as_done
from src.handlers.services.check_mark_as_done import is_mark_as_done_command
from src.handlers.start_handler import start_handler
from src.infrastructure.telegram import bot
from telebot import types

COMMANDS_HANDLERS = {
    "/start": start_handler,
    "/today": get_todo_list_on_today,
    "/t": get_todo_list_on_today,
}


@bot.message_handler(func=lambda _: True)
def message_router(m: types.Message):
    text = m.text.strip()

    if is_mark_as_done_command(text):
        return mark_as_done(message=m)
    if _callback := COMMANDS_HANDLERS.get(m.text):
        return _callback(message=m)
    else:
        return create_todo_handler(message=m)
