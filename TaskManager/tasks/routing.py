from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/task_notifications/$', consumers.TaskNotificationConsumer.as_asgi()),
]
