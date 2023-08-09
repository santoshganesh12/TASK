from rest_framework import serializers
from .models import Employee, Task
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

def send_notification(user, message):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f'user_{user.id}',  # Group name
        {
            'type': 'task.notification',
            'message': message,
        }
    )
