from django.contrib.auth.models import User
from rest_framework import serializers

from app.models.advertisement import Advertisement
from app.models.category import Category
from app.models.userProfile import UserProfile


class GetAuthTokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
