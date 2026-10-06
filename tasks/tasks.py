import time

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
