from django.urls import reverse
from django.conf import settings
from rest_framework import status
from rest_framework.test import APITestCase
from cert.models import CustomUser
from cert.serializers import CustomUserSerializer


class UserTests(APITestCase):
    def test_create_user(self):
        url = reverse('user_CR')
        data = {
            'name': 'tester',
            'call_sign': 'JEFF',
            'email': 'tester@test.com',
            'password': '1234',
            'user_id': 'test'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
