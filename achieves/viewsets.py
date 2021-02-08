from rest_framework import viewsets, permissions
from rest_framework.response import Response

from .models import Status, Achieve
from .serializers import StatusModelSerializer, AchieveModelSerializer


class StatusModelViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusModelSerializer
    permission_classes = []


class AchieveModelViewSet(viewsets.ModelViewSet):
    queryset = Achieve.objects.all()
    serializer_class = AchieveModelSerializer
    permission_classes = []
