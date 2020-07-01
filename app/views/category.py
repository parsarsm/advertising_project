from rest_framework import generics
from rest_framework.response import Response

from app.models.category import Category
from app.serializers.category import CategorySerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        response: Response = super().get(request, *args, **kwargs)
        response.content_type = 'application/json; charset=utf-8'
        return response
