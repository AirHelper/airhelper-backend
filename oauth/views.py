import requests
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.shortcuts import redirect
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status


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