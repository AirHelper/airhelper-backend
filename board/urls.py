from django.urls import path
from .views import BoardViewSet


post_cr = BoardViewSet.as_view({
    'post': 'create',
    'get': 'list'
})

post = BoardViewSet.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('post', post_cr, name='post_cr'),
    path('post/<int:pk>', post, name='post'),
]