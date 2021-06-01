import requests
from django.conf import settings
from django.contrib.auth.models import update_last_login
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from random import randint
from random_username.generate import generate_username

from cert.models import CustomUser
from cert.serializers import CustomUserSerializer
from .models import SocialUser
from .serializers import SocialUserSerializer


def create_bad_response(data):
    return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


def create_user_data(name, email, profile_image=None):
    data = {
        'user_id': generate_username()[0],
        'password': CustomUser.objects.make_random_password(
            length=14,
            allowed_chars="abcdefghjkmnpqrstuvwxyz0123456789"
        ),
        'email': email,
        'is_active': False,
        'is_staff': False,
        'name': name,
        'call_sign': 'anonymous' + str(randint(1, 1000)),
        'profile_image': profile_image
    }
    if profile_image is None:
        del data['profile_image']
    return data


def create_socialuser_data(user_id, social_user_id, social_type):
    return {
        'user': user_id,
        'social_user_id': social_user_id,
        'social_type': social_type
    }


def create_login_token(user):
    update_last_login(None, user)
    return Response({
        'user': CustomUserSerializer(user).data,
        'access': str(RefreshToken.for_user(user).access_token),
        'refresh': str(RefreshToken.for_user(user)),
        'lifetime': RefreshToken.for_user(user).access_token.lifetime,
    }, status=status.HTTP_200_OK)


def get_token_data(header, social_name):
    if social_name == settings.KAKAO:
        return requests.get(settings.KAKAO_API_URI + settings.KAKAO_TOKEN_INFO_URI, headers=header)


def get_login_data(header, social_name):
    if social_name == settings.KAKAO:
        return requests.post(settings.KAKAO_API_URI + settings.KAKAO_USER_INFO_URI, headers=header)


def get_user_data_by_token(request, social, token_type):
    if token_type == 'ACCESS_TOKEN':
        token = str(request.data.get('access'))
    elif token_type == 'AUTHORIZATION':
        token = str(request.headers.get('Authorization'))

    auth = {'Authorization': 'Bearer ' + token}
    access_token_data = get_token_data(auth, social)
    user_data = get_login_data(auth, social)

    if access_token_data.status_code != 200:
        return Response(status=status.HTTP_400_BAD_REQUEST, data=access_token_data.json())
    if user_data.status_code != 200:
        return Response(status=status.HTTP_400_BAD_REQUEST, data=user_data.json())
    return user_data.json()


def check_connected(user_data):
    if SocialUser.objects.filter(social_user_id=user_data.get('id')).exists():  # 이미 연동된 user
        connected_user = SocialUser.objects.filter(social_user_id=user_data.get('id')).get().user
        user_serializer = CustomUserSerializer(connected_user)
        if connected_user.is_active:
            return create_login_token(connected_user)
        return Response(status=status.HTTP_200_OK, data={'user': user_serializer.data})  # 추가정보 입력필요


def make_social_account(user_data, user_serializer, social):
    if user_serializer.is_valid():  # 회원가입
        new_user = user_serializer.save()
        socialuser_serializer = SocialUserSerializer(
            data=create_socialuser_data(new_user.id, user_data.get('id'), social)
        )
        if socialuser_serializer.is_valid():
            socialuser_serializer.save()
            return Response(status=status.HTTP_201_CREATED, data={'user': user_serializer.data})
        return Response(status=status.HTTP_400_BAD_REQUEST, data=socialuser_serializer.errors)
    return Response(status=status.HTTP_409_CONFLICT, data=user_serializer.errors)  # 이미 있는 이메일


def is_active_false_to_true(request):
    partial_data = request.data.copy()
    partial_data['is_active'] = True
    return partial_data
