def is_mark_as_done_command(text):
    return text and text.strip().lower().endswith("done")
