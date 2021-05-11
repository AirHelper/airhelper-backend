from django.urls import path
from .views import CustomUserViewSet


user_cr = CustomUserViewSet.as_view({
    'post': 'create',
    'get': 'list'
})

user = CustomUserViewSet.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('user', user_cr, name='user_CR'),
    path('user/<int:pk>', user, name='user'),
]