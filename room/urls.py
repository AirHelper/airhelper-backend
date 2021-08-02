from django.urls import path
from .views import (
    RoomViewSet
)

room_cr = RoomViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

room = RoomViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    path('room', room_cr, name='room_CR'),
    path('room/<int:pk>', room, name='room'),
]