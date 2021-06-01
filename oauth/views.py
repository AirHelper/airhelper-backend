import requests
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.shortcuts import redirect
from django.conf import settings
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.db import transaction
from django.shortcuts import redirect
from django.conf import settings

from cert.serializers import CustomUserSerializer
from cert.models import CustomUser
from .models import SocialUser
from .serializers import SocialUserSerializer, OauthUserSerializer
from .swagger import (
    SocialLoginSerializer, KakaoConnectionsDecorator, KakaoLoginDecorator
)
from .modules import (
    create_bad_response, create_login_token,  get_user_data_by_token, create_user_data,
    create_socialuser_data, make_social_account, check_connected, is_active_false_to_true
)

# 테스트하려고 임시로 만들어놓은 것, 완성후 삭제 예정
class KakaoSignInView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        client_id = 'de7b7a0ab725a968702ced050a21777b'
        return redirect(
            f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}"
            f"&redirect_uri={settings.KAKAO_REDIRECT_URI}&response_type=code"
        )


# 테스트하려고 임시로 만들어놓은 것, 완성후 삭제 예정
class KakaoSignInCallbackView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        code = request.GET.get("code")
        client_id = 'de7b7a0ab725a968702ced050a21777b'

        response = requests.get(
            f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}"
            f"&redirect_uri={settings.KAKAO_REDIRECT_URI}&code={code}"
        )
        response_json = response.json()
        print(response_json)

        error = response_json.get("error", None)

        if error is not None:
            return Response({"message": "INVALID_CODE"}, status=400)
        return Response(data=response_json, status=status.HTTP_200_OK, headers=response_json)


@method_decorator(KakaoLoginDecorator.Create(), name='create')
@method_decorator(KakaoLoginDecorator.Partial(), name='partial_update')
@method_decorator(KakaoLoginDecorator.Retrieve(), name='retrieve')
class KakaoViewSet(ModelViewSet):
    serializer_class = SocialLoginSerializer
    permission_classes = [AllowAny]

    def get_connected_user_object(self, id):
        social_user = get_object_or_404(SocialUser, user_id=id, social_type=settings.KAKAO)
        user = get_object_or_404(CustomUser, id=social_user.user_id)
        return user

    @action(detail=False, methods=['GET'])
    def retrieve(self, request):
        user_data = get_user_data_by_token(request, settings.KAKAO, 'AUTHORIZATION')
        if type(user_data) is Response:  # access_token 오류
            return user_data

        social_user = get_object_or_404(SocialUser, social_user_id=user_data.get('id'))
        user_serializer = CustomUserSerializer(social_user.user)
        return Response(user_serializer.data)

    @action(detail=False, methods=['POST'])
    @transaction.atomic
    def create(self, request):
        user_data = get_user_data_by_token(request, settings.KAKAO, 'ACCESS_TOKEN')
        if type(user_data) is Response:  # access_token 오류
            return user_data

        connected = check_connected(user_data)
        if connected:
            return connected

        user_serializer = CustomUserSerializer(data=create_user_data(
            user_data.get('kakao_account').get('profile').get('nickname'),
            user_data.get('kakao_account').get('email')
        ))
        return make_social_account(user_data, user_serializer, settings.KAKAO)

    @action(detail=True, methods=['PATCH'])
    def partial_update(self, request, user_id):
        user = self.get_connected_user_object(user_id)
        partial_data = is_active_false_to_true(request)
        serializer = OauthUserSerializer(user, data=partial_data)
        if serializer.is_valid():
            user_obj = serializer.save()
            return create_login_token(user_obj)
        return create_bad_response(serializer.errors)


@method_decorator(KakaoConnectionsDecorator.Create(), name='create')
@method_decorator(KakaoConnectionsDecorator.Retrieve(), name='retrieve')
@method_decorator(KakaoConnectionsDecorator.Destroy(), name='destroy')
class KakaoConnectionsViewSet(ModelViewSet):
    serializer_class = SocialLoginSerializer
    permission_classes = [AllowAny]

    @action(detail=True, methods=['GET'])
    def retrieve(self, request, user_id):
        connections = get_object_or_404(SocialUser, user_id=user_id, social_type=settings.KAKAO)
        self.check_object_permissions(self.request, connections)
        serializer = SocialUserSerializer(connections)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['POST'])
    @transaction.atomic
    def create(self, request, user_id):
        user_data = get_user_data_by_token(request, settings.KAKAO, 'ACCESS_TOKEN')
        if type(user_data) is Response:  # access_token 오류
            return user_data

        user = get_object_or_404(CustomUser, id=user_id)
        self.check_object_permissions(self.request, user)
        social_user_serializer = SocialUserSerializer(
            data=create_socialuser_data(user.id, user_data.get('id'), settings.KAKAO)
        )
        if social_user_serializer.is_valid():  # 연동이 안되어 있다면
            social_user_serializer.save()  # 연동
            return Response(status=status.HTTP_201_CREATED, data=social_user_serializer.data)
        return Response(status=status.HTTP_409_CONFLICT, data=social_user_serializer.errors)

    @action(detail=True, methods=['DELETE'])
    def destroy(self, request, user_id):
        user_connections = get_object_or_404(SocialUser, user_id=user_id, social_type=settings.KAKAO)
        self.check_object_permissions(self.request, user_connections)
        user_connections.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)