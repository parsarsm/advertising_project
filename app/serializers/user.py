from django.contrib.auth.models import User
from rest_framework import serializers

from app.models.userProfile import UserProfile
from app.serializers.userProfile import UserProfileSerializer


class UserSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer(read_only=False)

    class Meta:
        model = User
        fields = ('username', 'password', 'user_profile',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user_profile_data = validated_data.pop('user_profile')
        password = validated_data['password']
        user = User(**validated_data)
        user.set_password(password)
        user.save()

        user_profile = UserProfile.objects.create(user_id=user.id, **user_profile_data)

        return user

