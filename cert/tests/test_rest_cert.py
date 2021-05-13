from django.urls import reverse
from django.conf import settings
from rest_framework import status
from rest_framework.test import APITestCase
from cert.models import CustomUser
from cert.serializers import CustomUserSerializer
#
# class UserTests(APITestCase):
#     def setUp(self):

