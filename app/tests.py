from django.contrib.auth.models import User
from django.test import TestCase, Client

# Create your tests here.
from app.models import UserProfile


class UserLogInAndAuthTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='parsa', password='parsa')
        user_profile = UserProfile.objects.create(user_id=user.id, phone_number='+982134568423')
        # pass

    # def test_create_new_user(self):
        # c = Client()
        # response = self.client.post('/api/users/', {
        #     'username': 'poorya',
        #     'password': 'poorya',
        #     'user_profile': {
        #         'phone_number': '+989122469907'
        #     }
        # })
        # response = self.client.post(
        #     '/api/auth/get_token/',
        #     {
        #         'username': 'parsa',
        #         'password': 'parsa'
        #     }
        # )
        # self.assertEqual(response.status_code, 200,
        #                  vars(response)
                         # )
    #
    # def test_create_new_user(self):
    # c = Client()
    # response = c.post('/api/users/', {
    #     'username': 'john',
    #     'password': '12SmiThhkk',
    #     'user_profile': {
    #         'phone_number': '+989172369907'
    #     }
    # })
    # response = self.client.get('/auth/get_token/',
    #                            {
    # 'username': 'mytestuname',
    # 'password': 'myTespa88'
    # })
    # self.assertEqual(response.status_code, 200,
    #                  vars(response)
    # )

    def test_get_wrong_auth(self):
        response = self.client.get(
            '/auth/get_token/',
            {
                'username': '6546545',
                'password': '65411'
            }
        )
        self.assertEqual(response.status_code, 404)


class CategoryTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def test_url_retrieves_correct_result(self):
        response = self.client.get('/api/categories/')
        self.assertEqual(response.status_code, 200)
