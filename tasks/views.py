from rest_framework.decorators import api_view
from rest_framework.response import Response

from .tasks import slow_task


@api_view(["POST"])
def start_task(request):
    task = slow_task.delay()

    return Response(
        {
            "task_id": task.id,
            "status": "Task started",
        }
    )


@api_view(["GET"])
def task_status(request, task_id):
    task = slow_task.AsyncResult(task_id)

    return Response(
        {
            "task_id": task_id,
            "status": task.status,
            "result": task.result,
        }
    )
