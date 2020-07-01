import tempfile

from PIL import Image
from django.contrib.auth.models import User
from django.test import TestCase, Client

# TODO pipeline test auto test before deploy
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from app.models.category import Category
from app.models.userProfile import UserProfile


class totalTest(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

        Category.objects.create(name='test cat')

        self.user = User.objects.create(
            username='testtest',
            password='lb0i4igvih94F')
        UserProfile.objects.create(
            user=self.user,
            phone_number='09172369905'
        )

    def test_create_user(self):
        response = self.client.post(
            '/api/users/',
            {"username": "test_user", "password": "PrT33tPa",
             "user_profile": {"phone_number": "+98652122365"}}, format='json')
        token = response.data['token']
        self.assertTrue(token is not None)
        # self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        self.assertEqual(response.status_code, 201)

    # def test_get_auth_token(self):
    #     response = self.client.post(
    #         '/api-auth/',
    #         {
    #             'username': 'testtest',
    #             'password': 'lb0i4igvih94F'
    #         }
    #     )
    #     print('sssssssssssssssssssssssssssssssssssss')
    #     print(Token.objects.all())
    #     print(vars(response))
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_categories(self):
        response = self.client.get(
            '/api/categories/'
        )
        self.assertEqual(response.status_code, 200)

    def test_create_ad(self):
        image = Image.new('RGB', (100, 100))
        tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(tmp_file)
        tmp_file.seek(0)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + Token.objects.all()[0].key)
        response = self.client.post(
            '/api/advertisements/',
            {'title': 'ad one', 'description': 'des one', 'category': '1',
             'image': tmp_file},
            format='multipart'
        )
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

    def test_get_one_ad(self):
        image = Image.new('RGB', (100, 100))
        tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(tmp_file)
        tmp_file.seek(0)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + Token.objects.all()[0].key)
        response = self.client.post(
            '/api/advertisements/',
            {'title': 'ad one', 'description': 'des one', 'category': '1',
             'image': tmp_file},
            format='multipart'
        )
        response = self.client.get(
            '/api/advertisements/1/'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_ads(self):
        response = self.client.get(
            '/api/advertisements/'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
