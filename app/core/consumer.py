from channels.generic.websocket import AsyncWebsocketConsumer
import json


class ProgressConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("______CONN___________")
        self.task_id = self.scope['url_route']['kwargs']['task_id']
        await self.channel_layer.group_add(
            self.task_id,
            self.channel_name
        )
        await self.accept()
        await self.send(text_data=json.dumps({
            'message': 'You are now connected!'
        }))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.task_id,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print("******recieved msg****")
        print(text_data_json)

    async def task_progress(self, event):
        percentage_complete = event['percentage_complete']
        print("************percentage complete", percentage_complete)
        await self.send(text_data=json.dumps(
            {'percentage_complete': percentage_complete}))

    async def verification_valid(self, event):
        await self.send(text_data=json.dumps(event))
