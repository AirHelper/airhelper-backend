from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from urllib import parse
import json


class Game(AsyncWebsocketConsumer):
    http_user = True

    async def connect(self):
        self.room_name = parse.unquote(self.scope['url_route']['kwargs']['room_name'])
        self.room_group_name = 'game_%s' % self.room_name
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

# Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)

        await self.channel_layer.group_send(
            self.room_group_name,
            text_data_json
        )
