from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Room, AttendedUser
from .serializers import AttendedUserSerializer, AttendUserSerializer
from urllib import parse
import json


class CreateRoom(AsyncWebsocketConsumer):
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
        await self.delete_room()

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'user_disconnect',
                'user': self.my_user_id
            }
        )
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def user_disconnect(self, event):
        data = await self.get_attenduser()
        await self.send(text_data=data)

    @database_sync_to_async
    def delete_room(self):
        Room.objects.filter(id=self.room_name).delete()

# Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)

        if text_data_json['type'] == 'user_attend':
            self.my_user_id = text_data_json['user']
            await self.save_attenduser(text_data_json['user'], text_data_json['team'], text_data_json['is_admin'])

        await self.channel_layer.group_send(
            self.room_group_name,
            text_data_json
        )

    @database_sync_to_async
    def save_attenduser(self, user_id, team, is_admin=False):
        return AttendedUser.objects.create(
            user_id=user_id,
            team=team,
            room_id=self.room_name,
            is_admin=is_admin
        )

    async def user_attend(self, event):
        json_data = {'type':'user_attend'}
        json_data['data'] = await self.get_attenduser()

        await self.send(text_data=json.dumps(json_data))

    @database_sync_to_async
    def get_attenduser(self):
        attend_users = AttendedUser.objects.all()
        serializer = AttendedUserSerializer(attend_users, many=True)
        return serializer.data


class AttendRoom(AsyncWebsocketConsumer):
    http_user = True

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'game_%s' % self.room_name

        if await self.room_exists() is not True:
            self.my_user_id = 0
            return
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    @database_sync_to_async
    def room_exists(self):
        return Room.objects.filter(id=self.room_name).exists()

    async def disconnect(self, close_code):
        await self.delete_attend_user()
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'user_disconnect',
                'user': self.my_user_id
            }
        )
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def user_disconnect(self, event):
        data = await self.get_attenduser()
        await self.send(text_data=data)

    @database_sync_to_async
    def delete_attend_user(self):
        AttendedUser.objects.filter(user_id=self.my_user_id).delete()

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)

        if text_data_json['type'] == 'user_attend':  # 유저 방 입장
            self.my_user_id = text_data_json['user']
            await self.save_attenduser(text_data_json['user'], text_data_json['team'])

        await self.channel_layer.group_send(
            self.room_group_name,
            text_data_json
        )

    async def user_attend(self, event):
        json_data = {'type':'user_attend'}
        json_data['data'] = await self.get_attenduser()

        await self.send(text_data=json.dumps(json_data))

    @database_sync_to_async
    def save_attenduser(self, user_id, team):
        return AttendedUser.objects.create(
            user_id=user_id,
            team=team,
            room_id=self.room_name
        )

    @database_sync_to_async
    def get_attenduser(self):
        attend_users = AttendedUser.objects.all()
        serializer = AttendedUserSerializer(attend_users, many=True)
        return serializer.data

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))