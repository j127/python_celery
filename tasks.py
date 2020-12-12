from celery import Celery
from time import sleep

app = Celery(
    "tasks",
    broker="pyamqp://guest@localhost//",
    backend="db+sqlite:///db.sqlite3",
)


@app.task
def send_thing(text):
    sleep(5)
    return f"running task for '{text}'"
