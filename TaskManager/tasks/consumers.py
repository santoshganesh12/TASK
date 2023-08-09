from channels.generic.websocket import AsyncWebsocketConsumer
import json


class TaskNotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def notify(self, event):
        await self.send(text_data=json.dumps(event['message']))
