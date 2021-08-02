from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/create/(?P<room_name>\w+)/$', consumers.CreateRoom.as_asgi()),
    re_path(r'ws/attend/(?P<room_name>\w+)/$', consumers.AttendRoom.as_asgi()),
]