from rest_framework import permissions, generics

from app.models import Advertisement
from app.serializers import AdvertisementSerializer


class AdvertisementList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer


class AdvertisementDetails(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
