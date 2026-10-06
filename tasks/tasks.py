import time
from datetime import datetime

from celery import shared_task


@shared_task
def process_order(order_id):
    print(f"Processing order {order_id}...")

    time.sleep(5)

    print(f"Order {order_id} processed successfully!")

    return {
        "order_id": order_id,
        "status": "completed",
    }


from celery import shared_task


@shared_task(
    bind=True,
    max_retries=3,
    default_retry_delay=5,
)
def unstable_task(self):
    import random

    print("Attempting task...")

    if random.random() < 0.7:
        raise self.retry(exc=Exception("Temporary service failure"))

    print("Task completed successfully!")
    return "Success"


@shared_task(
    bind=True,
    max_retries=3,
    default_retry_delay=2,
)
def always_fails(self):
    try:
        raise ValueError("Something went wrong")
    except ValueError as exc:
        raise self.retry(exc=exc)


@shared_task
def scheduled_report():
    current_time = datetime.now().astimezone().isoformat()
    message = f"Scheduled report executed at {current_time}"

    print(message)
    return message