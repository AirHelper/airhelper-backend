from rest_framework import serializers
from drf_yasg.utils import swagger_auto_schema
"""
    Swagger Response or Body Serializer
"""


class RoomlistSerializer(serializers.Serializer):
    title = serializers.CharField(label='방 이름')
    password = serializers.CharField(label='방 비번')
    verboseLeft = serializers.IntegerField(label='레드팀 수')
    verboseRight = serializers.IntegerField(label='블루팀 수')
    time = serializers.IntegerField(label='게임 시간')
    gameType = serializers.IntegerField(label='게임 종류')


class RoomlistDecorator():
    def Retrieve():
        return swagger_auto_schema(
            operation_summary="방 목록 가져오기",
            operation_description="생성된 방 목록을 가져옵니다.",
            responses={
                200: RoomlistSerializer
            }
        )
