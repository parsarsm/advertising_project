from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework import validators
from django.contrib.auth import password_validation

from app.models import Advertisement, UserProfile, Category


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
        fields = ('username', 'user_profile',)

    def create(self, validated_data):
        print(validated_data)
        user_profile_data = validated_data.pop('user_profile')
        print(validated_data)
        user = User.objects.create(**validated_data)
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


# class UserSerializer(serializers.Serializer):
#     # advertisements = serializers.PrimaryKeyRelatedField(many=True, queryset=Advertisement.objects.all())
#     username = serializers.CharField(
#         max_length=30,
#         validators=[validators.UniqueValidator(queryset=User.objects.all())]
#     )
#     password = serializers.CharField(
#         max_length=15,
#     )
#     phone_number = serializers.CharField(
#         max_length=15,
#         validators=[validators.UniqueValidator(queryset=UserProfile.objects.all())]
#     )
#
#     @staticmethod
#     def validate_password(password):
#         password_validation.validate_password(
#             password
#         )
#         return password
#
#     def update(self, instance: User, validated_data):
#         # user_model_data = {x: y for (x, y) in validated_data.items() if x == 'username' or x == 'password'}
#         # user_profile_model_data = {x: y for (x, y) in validated_data.items() if x != 'username' and x != 'password'}
#         user_profile = UserProfile.objects.get(user_id=instance.id)
#         user_profile.phone_number = validated_data.get('phone_number', user_profile.phone_number)
#         user_profile.save()
#         return instance
#
#     def create(self, validated_data):
#         # user_model_data = {x: y for (x, y) in validated_data.items() if x == 'username' or x == 'password'}
#         # user_profile_model_data = {x: y for (x, y) in validated_data.items() if x != 'username' and x != 'password'}
#         user = User.objects.create(
#             username=validated_data['username'],
#             password=validated_data['password']
#         )
#         user_profile = UserProfile.objects.create(
#             user=user,
#             phone_number=validated_data['phone_number'])
#         return user


class AdvertisementSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Advertisement
        fields = ['id', 'title', 'owner']

# class AdvertisementSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=True, allow_blank=False, max_length=100)
#
#     def create(self, validated_data):
#         return Advertisement.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.save()
#         return instance
