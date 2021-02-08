from django.urls import path

from .viewsets import UserModelViewSet

user_list = UserModelViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

user_detail = UserModelViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

urlpatterns = [
    path('', user_list),
    path('<int:pk>/', user_detail)
]
