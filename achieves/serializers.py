from rest_framework import serializers

from .models import Status, Achieve


class StatusModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class AchieveModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achieve
        fields = '__all__'
