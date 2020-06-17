from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views
from .views.advertisements import AdvertisementList, AdvertisementDetails
from .views.category import CategoryList
from .views.image import Image
from .views.userAds import UserAds
from .views.users import UserList, UserDetails

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>', UserDetails.as_view()),
    path('advertisements/',
         AdvertisementList.as_view()),
    path('advertisements/<int:pk>/',
         AdvertisementDetails.as_view(),
         name='advertisement-details'),
    path('auth/get_token/', obtain_auth_token),
    path('categories/', CategoryList.as_view()),
    path('media/<str:name>/', Image.as_view()),
    path('user-ads/', UserAds.as_view())
]
