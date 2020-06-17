import logging

from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework import validators
from django.contrib.auth import password_validation
from rest_framework.fields import CurrentUserDefault

from app.models import Advertisement, UserProfile, Category


class UserAdsSerializer(serializers.Serializer):
    id = serializers.IntegerField()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ('title', 'description', 'owner', 'category', 'image', 'active')
        extra_kwargs = {
            'owner': {'read_only': True},
            'active': {'read_only': True}
        }

    def save(self, **kwargs):
        kwargs['owner'] = User.objects.get_by_natural_key(self.context['request'].user)
        super(AdvertisementSerializer, self).save(**kwargs)


class GetAuthTokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('phone_number',)


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


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'subcategories')

    def get_fields(self):
        fields = super(CategorySerializer, self).get_fields()
        fields['subcategories'] = CategorySerializer(many=True)
        return fields
