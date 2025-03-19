from ex2.celery_task import long_task


result = long_task.apply_async(args=[15], countdown=3)
print(f"Task send, id: {result.id}")
print("wait")
print(result.get(timeout=100))