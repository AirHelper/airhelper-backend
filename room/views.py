from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from rest_framework.permissions import AllowAny
from .serializers import RoomSerializer, AttendedUserSerializer
from .swagger import RoomDecorator, AttendedUserDecorator
from rest_framework import status
from django.db import transaction
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Room, AttendedUser
from django.shortcuts import get_object_or_404, get_list_or_404


@method_decorator(RoomDecorator.Create(), name='create')
@method_decorator(RoomDecorator.Retrieve(), name='retrieve')
@method_decorator(RoomDecorator.List(), name='list')
class RoomViewSet(ModelViewSet):
    serializer_class = RoomSerializer
    permission_classes = [AllowAny]
    queryset = Room.objects.all()


@method_decorator(AttendedUserDecorator.Create(), name='create')
@method_decorator(AttendedUserDecorator.Retrieve(), name='retrieve')
@method_decorator(AttendedUserDecorator.Destroy(), name='destroy')
class AttendedUserViewSet(ModelViewSet):
    serializer_class = AttendedUserSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=['GET'])
    def retrieve(self, request, room_id):
        users = get_list_or_404(AttendedUser, room=room_id)
        serializer = AttendedUserSerializer(users, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @action(detail=False, methods=['POST'])
    def create(self, request):
        return Response(status=status.HTTP_200_OK)

    @action(detail=False, methods=['DELETE'])
    def destroy(self, request):
        return Response(status=status.HTTP_200_OK)