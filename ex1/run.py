from ex1.celery_test_1 import add


result = add.delay(4, 6)
print(f"Task sent! Task id: {result.id}")
print(f"Result: {result.get(timeout=50)}")
print("Finish")