from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from urllib import parse
from .models import Game as Games
import json, time, datetime


class Game(AsyncWebsocketConsumer):
    http_user = True

    async def connect(self):
        self.game_id = parse.unquote(self.scope['url_route']['kwargs']['game_id'])
        self.game_name = 'game_%s' % self.game_id
        # Join room group
        await self.channel_layer.group_add(
            self.game_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.game_name,
            self.channel_name
        )

# Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)

        # if text_data_json['type'] == 'timer':  # 게임 타이머
        #     self.time = await self.get_gameTime()

        await self.channel_layer.group_send(
            self.game_name,
            text_data_json
        )

    async def timer(self, event):
        now = datetime.datetime.now()
        time = await self.get_gameTime()
        after = now + datetime.timedelta(minutes=time.time)
        json_data = {
            'type': 'timer',
            'start_time': "%02d:%02d:%02d" % (now.hour, now.minute, now.second),
            'end_time': "%02d:%02d:%02d" % (after.hour, after.minute, after.second)
        }
        await self.send(text_data=json.dumps(json_data))

    @database_sync_to_async
    def get_gameTime(self):
        return Games.objects.filter(id=self.game_id).get()

    async def location(self, event):
        await self.send(text_data=json.dumps(event))