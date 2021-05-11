from django.test import TestCase
from cert.models import CustomUser
from cert.serializers import CustomUserSerializer


class CustomUserModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(
            password='test',
            user_id="testuser",
            email='dev@dev.com',
            name='Jun',
            call_sign='JEFF'
        )
        self.user.set_password('1234')
        self.user.save()
        self.serialized_user = CustomUserSerializer(self.user).data

    def test_create_models(self):
        self.user1 = CustomUser.objects.create(
            password='test',
            user_id="testuser1",
            email='dev1@dev.com',
            name='Jun',
            call_sign='JEFF1'
        )
        self.user1.set_password('1234')
        self.user1.save()
        self.serialized_user1 = CustomUserSerializer(self.user1).data