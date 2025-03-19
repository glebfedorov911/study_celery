from celery import Celery

import time


app = Celery(
    "tasks", 
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

@app.task 
def long_task(x):
    time.sleep(x)
    return f"Result: {x ** 2}"