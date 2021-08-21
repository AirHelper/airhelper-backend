from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from rest_framework.permissions import AllowAny
from .serializers import BoardSerializer, BoardMediaSerializer, BoardCommentSerializer
from .swagger import BoardDecorator
from rest_framework import status
from django.db import transaction
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Board, BoardMedia, BoardComment
from django.shortcuts import get_object_or_404, get_list_or_404


@method_decorator(BoardDecorator.Create(), name='create')
@method_decorator(BoardDecorator.List(), name='list')
@method_decorator(BoardDecorator.Retrieve(), name='retrieve')
@method_decorator(BoardDecorator.Partial(), name='partial_update')
@method_decorator(BoardDecorator.Destroy(), name='destroy')
class BoardViewSet(ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer