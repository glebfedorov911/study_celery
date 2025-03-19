from celery import Celery


app = Celery(
    "myapp",
    broker="redis://localhost:6379/0"
)

app.conf.beat_schedule = {
    "my_task": {
        "task": "beat1.celery_app.my_task",
        'schedule': 30.0
    }
}


@app.task
def my_task():
    print("task")
    return "jfdsjfdsjfds"