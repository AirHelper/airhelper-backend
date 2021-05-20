from django.urls import reverse
from django.conf import settings
from rest_framework import status
from rest_framework.test import APITestCase
from cert.models import CustomUser
from cert.serializers import CustomUserSerializer


class UserTests(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(
            password='test',
            user_id="testuser111",
            email='dev11@dev.com',
            name='Jun11',
            call_sign='JEFF111'
        )
        self.user.set_password('1234')
        self.user.save()

    def test_create_user(self):
        # post
        url = reverse('user_CR')
        data = {
            'name': 'tester',
            'call_sign': 'JEFF',
            'email': 'tester@test.com',
            'password': '1234',
            'user_id': 'test'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(CustomUser.objects.count(), 2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        temp = response.data

        # get
        url = reverse('user', kwargs={'pk': response.data['id']})
        response = self.client.get(url, format='json')
        self.assertEqual(response.data, temp)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # patch
        url = reverse('user', kwargs={'pk': response.data['id']})
        data = {
            'name': 'modifyed_tester'
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(CustomUser.objects.filter(id=response.data['id']).first().name, 'modifyed_tester')

        # delete
        url = reverse('user', kwargs={'pk': response.data['id']})
        response = self.client.delete(url, format='json')
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_create_user_no_name(self):
        url = reverse('user_CR')
        data = {
            'call_sign': 'nicktest',
            'email': 'email@dev.com',
            'user_id': 'test_id',
            'password': 'dev1!'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_no_callsign(self):
        url = reverse('user_CR')
        data = {
            'name': 'testuser',
            'email': 'email@dev.com',
            'user_id': 'test_id',
            'password': 'dev1!'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_no_email(self):
        url = reverse('user_CR')
        data = {
            'name': 'testuser',
            'call_sign': 'nicktest',
            'user_id': 'test_id',
            'password': 'dev1!'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_no_user_id(self):
        url = reverse('user_CR')
        data = {
            'name': 'testuser',
            'call_sign': 'nicktest',
            'email': 'email@dev.com',
            'password': 'dev1!'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_no_password(self):
        url = reverse('user_CR')
        data = {
            'name': 'testuser',
            'call_sign': 'nicktest',
            'email': 'email@dev.com',
            'user_id': 'test_id',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_user_list(self):
        url = reverse('user_CR')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user(self):
        url = reverse('user', kwargs={'pk': self.user.id})
        response = self.client.get(url)
        serialized_user = CustomUserSerializer(self.user).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serialized_user)
