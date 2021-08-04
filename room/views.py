from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from rest_framework.permissions import AllowAny
from .serializers import RoomSerializer, AttendedUserSerializer, AttendUserSerializer
from .swagger import RoomDecorator, AttendedUserDecorator, GameAttendUserSerializer
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
    serializer_class = GameAttendUserSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=['GET'])
    def retrieve(self, request, room_id):  # 특정 방에 입장한 유저 목록
        users = get_list_or_404(AttendedUser, room=room_id)
        serializer = AttendedUserSerializer(users, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @action(detail=False, methods=['POST'])  # 특정 방에 입장시키기
    def create(self, request):
        serializer = AttendUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    @action(detail=False, methods=['DELETE'])  # 특정 방에서 퇴장시키기
    def destroy(self, request):
        attend_user = get_object_or_404(AttendedUser, user=request.data['user'], room=request.data['room'])
        attend_user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)