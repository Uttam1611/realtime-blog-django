from channels.generic.websocket import AsyncWebsocketConsumer
import json

class PostsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('posts', self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('posts', self.channel_name)

    async def receive(self, text_data):
        # Echo any data back or handle messages
        await self.channel_layer.group_send(
            'posts',
            {
                'type': 'send_new_post',
                'post': json.loads(text_data),
            }
        )

    async def send_new_post(self, event):
        await self.send(text_data=json.dumps({'post': event['post']}))
