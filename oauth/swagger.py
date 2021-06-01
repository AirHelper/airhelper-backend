from rest_framework import serializers
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from cert.serializers import CustomUserSerializer
from cert.swagger import LoginResponseSerializer
from .serializers import SocialUserSerializer
"""
    Swagger Response or Body Serializer
"""


class SocialLoginSerializer(serializers.Serializer):
    access = serializers.CharField(label='접속 토큰')


class SocialaddDataSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='회원번호')
    call_sign = serializers.CharField(label='콜사인', max_length=60)


class KakaoLoginDecorator():
    def Create():
        return swagger_auto_schema(
            operation_summary="Kakao",
            operation_description="카카오로 로그인/가입한다.",
            request_body=SocialLoginSerializer,
            responses={
                201: CustomUserSerializer,
                200: LoginResponseSerializer,
                409: openapi.Response('이미 가입된 이메일 존재')
            }
        )

    def Retrieve():
        return swagger_auto_schema(
            operation_summary="Kakao",
            operation_description="카카오로 로그인한 사용자 정보를 불러온다.",
            manual_parameters=[
                openapi.Parameter(
                    'Authorization', openapi.IN_HEADER, description="접속 토큰", type=openapi.TYPE_STRING,
                    required=True
                )
            ],
            responses={
                200: CustomUserSerializer
            }
        )

    def Partial():
        return swagger_auto_schema(
            operation_summary="Kakao",
            operation_description="카카오 최초 로그인 후 추가 정보를 입력받는다.",
            request_body=SocialaddDataSerializer,
            responses={
                200: LoginResponseSerializer
            }
        )


class KakaoConnectionsDecorator():
    def Retrieve():
        return swagger_auto_schema(
            operation_summary="Kakao Connections",
            operation_description="카카오 계정 연동정보 가져오기",
            responses={
                200: SocialUserSerializer
            }
        )

    def Create():
        return swagger_auto_schema(
            operation_summary="Kakao Connections",
            operation_description="카카오 계정 연동",
            request_body=SocialLoginSerializer,
            responses={
                201: SocialUserSerializer
            }
        )

    def Destroy():
        return swagger_auto_schema(
            operation_summary="Kakao Connections",
            operation_description="카카오 계정 연동해제"
        )

