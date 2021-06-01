from django.urls import path
from .views import (
    KakaoSignInView, KakaoSignInCallbackView,  # 테스트 용
    KakaoViewSet, KakaoConnectionsViewSet
)

kakao = KakaoViewSet.as_view({
    'get': 'retrieve',
    'post': 'create'
})

kakao_patch = KakaoViewSet.as_view({
    'patch': 'partial_update'
})

kakaoconnections = KakaoConnectionsViewSet.as_view({
    'get': 'retrieve',
    'post': 'create',
    'delete': 'destroy'
})

urlpatterns = [
    path('kakao', kakao, name='kakao'),
    path('kakao/<int:user_id>', kakao_patch, name='kakao_patch'),
    path('kakao/connections/<int:user_id>', kakaoconnections, name='kakaoconnections'),
    # 테스트 하기 위해 만들어놓은 URL
    path('kakaotest/login', KakaoSignInView.as_view(), name='kakaotestlogin'),
    path('kakao/login/callback/', KakaoSignInCallbackView.as_view(), name='callback'),
]