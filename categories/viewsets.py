from rest_framework import viewsets

from .models import Category
from .serializers import CategoryModelSerializer


class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    permission_classes = []
