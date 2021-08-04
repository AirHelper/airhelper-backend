from django.urls import path
from .views import (
    RoomViewSet, AttendedUserViewSet
)

room_cr = RoomViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

room = RoomViewSet.as_view({
    'get': 'retrieve'
})

attend_user_c = AttendedUserViewSet.as_view({
    'post': 'create',
    'delete': 'destroy'
})

attend_user = AttendedUserViewSet.as_view({
    'get': 'retrieve',
})

urlpatterns = [
    path('room', room_cr, name='room_CR'),
    path('room/<int:pk>', room, name='room'),
    path('attend', attend_user_c, name='attend_user_C'),
    path('attend/<int:room_id>', attend_user, name='attend_user'),
]