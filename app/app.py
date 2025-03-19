from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn
import os

from app.utils import generate_report


app = FastAPI()

@app.post("/report/")
async def create_report():
    task = generate_report.apply_async()
    return {
        "message": "Отчет генерируется",
        "task_id": task.id
    }

@app.get("/report/{task_id}")
async def get_report(task_id: str):
    task = generate_report.AsyncResult(task_id)

    if task.ready():
        report_path = task.result
        return FileResponse(report_path, filename=report_path.split('/')[-1])
    else:
        return {
            "message": "Отчет все еще генерируется",
            "task_id": task.id
        }
    
if __name__ == "__main__":
    uvicorn.run("app.app:app", reload=True)