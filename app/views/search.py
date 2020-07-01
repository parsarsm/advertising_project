from rest_framework import permissions, generics
from rest_framework.response import Response

from app.models.advertisement import Advertisement
from app.serializers.advertisement import AdvertisementSerializer


class AdvertisementListSearch(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = AdvertisementSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Advertisement.objects.all()
        query = self.request.query_params.get('query', None)
        if query is not None:
            queryset = queryset.filter(title__icontains=query) | \
                       queryset.filter(description__icontains=query)
        return queryset

    def get(self, request, *args, **kwargs):
        response: Response = super().get(request, *args, **kwargs)
        response.content_type = 'application/json; charset=utf-8'

        return response
