from celery import Celery

import time


app = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

@app.task
def add(x, y):
    time.sleep(20)
    return x+y