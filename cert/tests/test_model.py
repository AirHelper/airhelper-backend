from django.test import TestCase
from cert.models import CustomUser, UserManager
from cert.serializers import CustomUserSerializer, CreateUserSerializer
import os


class CustomUserModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(
            password='test',
            user_id="testuser321321",
            email='dev321312@dev.com',
            name='Ju321n',
            call_sign='JEFF3213213'
        )
        self.user.set_password('1234')
        self.user.save()
        self.serialized_user = CustomUserSerializer(self.user).data
        self.assertEqual(self.user.has_perm('cert'), True)
        self.assertEqual(self.user.has_module_perms('cert'), True)

    def test_create_models(self):  # 생성테스트
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

        self.basic_user = CustomUser.objects.create_user(
            user_id='test',
            email="cartoonpoet@naver.com",
            password='dfsdfsd',
            name='jun3213',
            call_sign='MAD'
        )
        self.assertEqual(CustomUser.objects.count(), 3)

        self.staff_user = CustomUser.objects.create_staffuser(
            user_id='staff',
            email='staff@naver.com',
            name='staff_person',
            call_sign='STAFF',
            password='1232'
        )
        self.assertEqual(CustomUser.objects.count(), 4)

        self.super_user = CustomUser.objects.create_superuser(
            user_id='root',
            email='root@root.com',
            name='root',
            call_sign='ROOT',
            password='root'
        )
        self.assertEqual(CustomUser.objects.count(), 5)
