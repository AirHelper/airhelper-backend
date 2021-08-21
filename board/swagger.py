from rest_framework import serializers
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import BoardSerializer, BoardCommentSerializer, BoardMediaSerializer


"""
    Swagger Response or Body Serializer
"""


class BoardDecorator():
    def Create():
        return swagger_auto_schema(
            operation_summary="게시물 작성",
            operation_description="게시물 작성",
            request_body=BoardSerializer,
            responses={
                201: BoardSerializer
            }
        )

    def List():
        return swagger_auto_schema(
            operation_summary="게시물 리스트",
            operation_description="게시물 리스트",
            responses={
                200: BoardSerializer
            }
        )

    def Retrieve():
        return swagger_auto_schema(
            operation_summary="특정 게시물 확인",
            operation_description="특정 게시물 확인",
            responses={
                200: BoardSerializer
            }
        )

    def Partial():
        return swagger_auto_schema(
            operation_summary="특정 게시물 수정",
            operation_description="특정 게시물 수정",
            request_body=BoardSerializer,
            responses={
                201: BoardSerializer
            }
        )

    def Destroy():
        return swagger_auto_schema(
            operation_summary="특정 게시물 삭제",
            operation_description="특정 게시물 삭제"
        )

