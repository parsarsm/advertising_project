from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetails.as_view()),
    path('advertisements/',
         views.AdvertisementList.as_view()),
    path('advertisements/<int:pk>/',
         views.AdvertisementDetails.as_view(),
         name='advertisement-details'),
    path('auth/get_token/', obtain_auth_token),
    path('categories/', views.CategoryList.as_view())
]
