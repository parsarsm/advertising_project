from django.contrib.auth.models import User
from rest_framework import serializers

from app.models.advertisement import Advertisement


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
