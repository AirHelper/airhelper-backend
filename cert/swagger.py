from rest_framework import serializers
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import CustomUserSerializer


"""
    Swagger Response or Body Serializer
"""


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
