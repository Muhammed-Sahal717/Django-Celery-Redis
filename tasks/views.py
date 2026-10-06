from rest_framework.decorators import api_view
from rest_framework.response import Response

from .tasks import process_order


@api_view(["POST"])
def start_task(request):
    order_id = request.data.get("order_id")

    if order_id is None:
        return Response(
            {"error": "order_id is required"},
            status=400,
        )

    task = process_order.delay(order_id)

    return Response(
        {
            "task_id": task.id,
            "status": "Order processing started",
            "order_id": order_id,
        },
        status=202,
    )


@api_view(["GET"])
def task_status(request, task_id):
    task = process_order.AsyncResult(task_id)

    return Response(
        {
            "task_id": task_id,
            "status": task.status,
            "result": task.result if task.successful() else None,
        }
    )
