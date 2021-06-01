from rest_framework import serializers
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import CustomUserSerializer


"""
    Swagger Response or Body Serializer
"""


class LoginUserResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='PK', required=False)
    last_login = serializers.DateTimeField(label='마지막 로그인', required=False)
    user_id = serializers.CharField(label='아이디', max_length=50, required=False)
    email = serializers.EmailField(label='이메일', max_length=254, required=False)
    name = serializers.CharField(label='이름', max_length=60, required=False)
    call_sign = serializers.CharField(label='닉네임', max_length=60, required=False)
    profile_image = serializers.CharField(label='프로필사진', required=False)
    is_active = serializers.BooleanField(label='활성화여부', required=False)


class LoginResponseSerializer(serializers.Serializer):
    user = LoginUserResponseSerializer(label='유저정보', required=False)
    access = serializers.CharField(label='access토큰', required=False)
    refresh = serializers.CharField(label='refresh토큰', required=False)
    lifetime = serializers.FloatField(label='access토큰 남은시간', required=False)


class CustomUserDecorator():
    def Create():
        return swagger_auto_schema(
            operation_summary="User 회원가입",
            operation_description="User 회원가입",
            request_body=CustomUserSerializer,
            responses={
                201: CustomUserSerializer
            }
        )

    def List():
        return swagger_auto_schema(
            operation_summary="User 리스트 확인",
            operation_description="User 리스트 확인",
            responses={
                200: CustomUserSerializer
            }
        )

    def Retrieve():
        return swagger_auto_schema(
            operation_summary="PK User 확인",
            operation_description="특정 User 확인",
            responses={
                200: CustomUserSerializer
            }
        )

    def Partial():
        return swagger_auto_schema(
            operation_summary="PK User 수정",
            operation_description="특정 User 수정",
            responses={
                201: CustomUserSerializer
            }
        )

    def Destroy():
        return swagger_auto_schema(
            operation_summary="PK User 삭제",
            operation_description="특정 User 삭제"
        )
