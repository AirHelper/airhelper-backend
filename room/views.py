from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from rest_framework.permissions import AllowAny
from .serializers import RoomSerializer
from .swagger import RoomDecorator
from rest_framework import status
from django.db import transaction
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Room


@method_decorator(RoomDecorator.Create(), name='create')
@method_decorator(RoomDecorator.Retrieve(), name='retrieve')
@method_decorator(RoomDecorator.List(), name='list')
class RoomViewSet(ModelViewSet):
    serializer_class = RoomSerializer
    permission_classes = [AllowAny]
    queryset = Room.objects.all()
