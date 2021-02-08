from django.urls import path

from .viewsets import StatusModelViewSet, AchieveModelViewSet

status_list = StatusModelViewSet.as_view({'get': 'list'})

achieve_list = AchieveModelViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

achieve_detail = AchieveModelViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

urlpatterns = [
    path('', achieve_list),
    path('<int:pk>/', achieve_detail),
    path('statuses/', status_list)
]
