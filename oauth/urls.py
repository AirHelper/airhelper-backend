from django.urls import path
from .views import (
    KakaoSignInView, KakaoSignInCallbackView,  # 테스트 용
)
urlpatterns = [
    #path('kakao', kakao, name='kakao'),
    # 테스트 하기 위해 만들어놓은 URL
    path('kakaotest/login', KakaoSignInView.as_view(), name='kakaotestlogin'),
    path('kakao/login/callback/', KakaoSignInCallbackView.as_view(), name='callback'),
]