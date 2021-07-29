from .swagger import RoomlistDecorator
from rest_framework.viewsets import ModelViewSet
from django.utils.decorators import method_decorator
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from channels.layers import get_channel_layer


# Create your views here.
@method_decorator(RoomlistDecorator.Retrieve(), name='retrieve')
class RoomViewSet(ModelViewSet):  # 카카오 로그인/회원가입
    serializer_class = RoomlistDecorator
    permission_classes = [AllowAny]

    @action(detail=False, methods=['GET'])
    def retrieve(self, request):
        channel_layer = get_channel_layer()
        print('dddddddd'+channel_layer)
        return Response(data=1, status=status.HTTP_200_OK)

