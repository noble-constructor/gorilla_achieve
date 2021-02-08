from django.urls import path

from .viewsets import CategoryModelViewSet

category_list = CategoryModelViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

category_detail = CategoryModelViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

urlpatterns = [
    path('', category_list),
    path('<int:pk>/', category_detail)
]
