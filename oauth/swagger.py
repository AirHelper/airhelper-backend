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
    call_sign = serializers.CharField(label='콜사인', max_length=60)

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField(label='리프레시 토큰')


class KakaoLoginDecorator():
    def Create():
        return swagger_auto_schema(
            operation_summary="카카오 로그인/회원가입",
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
            operation_summary="카카오 로그인정보 불러오기",
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
            operation_summary="카카오 추가 정보 입력",
            operation_description="카카오 최초 로그인 후 추가 정보를 입력받는다.",
            request_body=SocialaddDataSerializer,
            responses={
                200: LoginResponseSerializer
            }
        )


class KakaoConnectionsDecorator():
    def Retrieve():
        return swagger_auto_schema(
            operation_summary="카카오 계정 연동정보 가져오기",
            operation_description="카카오 계정 연동정보 가져오기",
            responses={
                200: SocialUserSerializer
            }
        )

    def Create():
        return swagger_auto_schema(
            operation_summary="카카오 계정 연동",
            operation_description="카카오 계정 연동",
            request_body=SocialLoginSerializer,
            responses={
                201: SocialUserSerializer
            }
        )

    def Destroy():
        return swagger_auto_schema(
            operation_summary="카카오 계정 연동 해제",
            operation_description="카카오 계정 연동해제"
        )


class LogoutDecorator():
    def Destroy():
        return swagger_auto_schema(
            operation_summary="로그아웃",
            operation_description="우리 서비스를 로그아웃 시킨다. 토큰을 만료시킨다.",
            request_body= LogoutSerializer,
            responses={
                204: openapi.Response('로그아웃'),
                400: openapi.Response('잘못된 refresh_token')
            }
        )