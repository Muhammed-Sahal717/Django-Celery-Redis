from django.urls import path

from .views import start_task, task_status


urlpatterns = [
    path("start/", start_task, name="start-task"),
    path("status/<str:task_id>/", task_status, name="task-status"),
]
