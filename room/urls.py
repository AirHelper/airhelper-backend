from django.urls import path
from .views import (
    RoomViewSet
)

room = RoomViewSet.as_view({
    'get': 'retrieve',
})

urlpatterns = [
    path('list', room, name='room'),
]
