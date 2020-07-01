from rest_framework import permissions, generics
from rest_framework.response import Response

from app.models.advertisement import Advertisement
from app.serializers.advertisement import AdvertisementSerializer


class AdvertisementList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # queryset = Advertisement.objects.all()
    queryset = Advertisement.objects.filter(active=True)
    serializer_class = AdvertisementSerializer

    def get(self, request, *args, **kwargs):
        response: Response = super().get(request, *args, **kwargs)
        response.content_type = 'application/json; charset=utf-8'
        return response


class AdvertisementDetails(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

    def get(self, request, *args, **kwargs):
        response: Response = super().get(request, *args, **kwargs)
        response.content_type = 'application/json; charset=utf-8'
        return response
