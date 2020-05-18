from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import status, permissions, generics
from rest_framework.authtoken.models import Token
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from app.models import Advertisement, Category
from app.permissions import IsOwnerOrReadOnly
from app.serializers import AdvertisementSerializer, UserSerializer, GetAuthTokenSerializer, CategorySerializer


class UserList(APIView):
    def post(self, request: Request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user: User = serializer.save()
            token = Token.objects.get(user_id=user.id)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors.update({'rest': 'test'}), status=status.HTTP_400_BAD_REQUEST)


class UserDetails(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes =


class AdvertisementList(APIView):

    def get(self, request):
        advertisements = Advertisement.objects.all()
        serializer = AdvertisementSerializer(advertisements, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AdvertisementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    permission_classes = [permissions.IsAuthenticated]


class AdvertisementDetails(APIView):
    def get_object(self, pk):
        try:
            return Advertisement.objects.get(pk=pk)
        except Advertisement.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        advertisement = self.get_object(pk)
        serializer = AdvertisementSerializer(advertisement)
        return Response(serializer.data)

    def put(self, request, pk):
        advertisement = self.get_object(pk)
        serializer = AdvertisementSerializer(advertisement, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        advertisement = self.get_object(pk)
        advertisement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
