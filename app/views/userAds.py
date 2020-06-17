from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import views

from app.models import Advertisement
from app.serializers import UserAdsSerializer, AdvertisementSerializer


class UserAds(views.APIView):
    def get(self, request: Request):
        user = User.objects.get_by_natural_key(request.data['username'])
        ads = Advertisement.objects.filter(owner_id=user.id)
        print(ads)
        return Response(data=AdvertisementSerializer(ads,many=True).data, status=status.HTTP_200_OK)
