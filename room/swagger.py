from rest_framework import serializers
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import RoomSerializer
"""
    Swagger Response or Body Serializer
"""


class RoomDecorator():
    def Create():
        return swagger_auto_schema(
            operation_summary="방 생성",
            operation_description="방 생성하기",
            request_body=RoomSerializer,
            responses={
                201: RoomSerializer
            }
        )

    def List():
        return swagger_auto_schema(
            operation_summary="방 목록",
            operation_description="방 리스트 불러오기",
            responses={
                200: RoomSerializer
            }
        )

    def Retrieve():
        return swagger_auto_schema(
            operation_summary="특정 방 정보",
            operation_description="특정 방 정보를 불러온다.",
            responses={
                200: RoomSerializer
            }
        )


