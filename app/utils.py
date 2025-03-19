from app.mycelery import app as celery_app

import time
import os 
import random


@celery_app.task
def generate_report():
    print("Генерация отчета")
    time.sleep(10)

    dirname = "app/reports"
    if not os.path.exists(dirname):
        os.mkdir(dirname)

    num = random.randint(1, 100_000)
    filepath = f"{dirname}/report_num_{num}.txt"
    with open(filepath, 'w') as file:
        file.write(f"Отчет номер {num}")

    print("Отчет сгенерирован")
    return filepath