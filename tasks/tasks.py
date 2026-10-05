import time

from celery import shared_task


@shared_task
def slow_task():
    print("Task started...")

    time.sleep(10)

    print("Task finished!")

    return "Slow task completed"
