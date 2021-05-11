from datetime import datetime
import time
from django.shortcuts import get_object_or_404
from django.db import transaction
from django.contrib.auth.models import update_last_login
from django.utils.decorators import method_decorator
from rest_framework import status
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt import authentication
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from .models import CustomUser
from .serializers import (
    CustomUserSerializer
)
from .swagger import (
    CustomUserDecorator
)


@method_decorator(CustomUserDecorator.Create(), name='create')
@method_decorator(CustomUserDecorator.List(), name='list')
@method_decorator(CustomUserDecorator.Retrieve(), name='retrieve')
@method_decorator(CustomUserDecorator.Partial(), name='partial_update')
@method_decorator(CustomUserDecorator.Destroy(), name='destroy')
class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

