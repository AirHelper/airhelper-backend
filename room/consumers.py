from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from asgiref.sync import sync_to_async
from .models import Room, AttendedUser
from .serializers import AttendedUserSerializer, AttendUserSerializer
from urllib import parse
from django.core import serializers
from .views import AttendedUserViewSet
import json

class CreateRoom(AsyncWebsocketConsumer):
    http_user = True

    async def connect(self):
        self.room_name = parse.unquote(self.scope['url_route']['kwargs']['room_name'])
        self.room_group_name = 'game_%s' % self.room_name
        print(self.room_name)
        print(self.room_group_name)
        print('채녈명 : '+self.channel_name)

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.delete_room()

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'all_disconnect',
                'message': 'disconnect'
            }
        )
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    @database_sync_to_async
    def delete_room(self):
        Room.objects.filter(id=self.room_name).delete()

    async def user_attend(self, event):
        attended_users = AttendedUser.objects.filter(room=self.room_name).all()
        serializer = AttendedUserSerializer(attended_users, many=True)
        await self.send(text_data=serializer.data)


class AttendRoom(AsyncWebsocketConsumer):
    http_user = True

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
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

    async def user_attend(self, event):
        attend_user = await self.save_attenduser(event['user'], event['team'])
        data = await self.create_attenduser()
        await self.send(text_data=data)

    @database_sync_to_async
    def save_attenduser(self, user_id, team):
        return AttendedUser.objects.create(
            user_id=user_id,
            team=team,
            room_id=self.room_name
        )

    @database_sync_to_async
    def create_attenduser(self):
        attend_users = AttendedUser.objects.all()
        serializer = AttendedUserSerializer(attend_users, many=True)
        return json.dumps(serializer.data)

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))