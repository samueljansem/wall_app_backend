from rest_framework.test import APITestCase, force_authenticate
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model


User = get_user_model()


class TestSetup(APITestCase):

    def setUp(self):
        self.signup_url = reverse('signup')
        self.login_url = reverse('login')
        self.list_posts_url = reverse('list_posts')
        self.create_post_url = reverse('create_post')

        return super().setUp()

    def test_signup(self):
        credentials = {
            'username': 'testuser',
            'email': 'test.user@gmail.com',
            'password': '12345678'
        }

        print(self.signup_url)

        response = self.client.post(self.signup_url, credentials)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def authenticate(self):
        self.client.post(self.signup_url, {
            'username': 'testuser',
            'email': 'test.user@gmail.com',
            'password': '12345678'
        })

        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': '12345678'
        })

        token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    def test_login(self):
        self.client.post(self.signup_url, {
            'username': 'testuser',
            'email': 'test.user@gmail.com',
            'password': '12345678'
        })

        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': '12345678'
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_posts(self):
        response = self.client.get(self.list_posts_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post_authenticated(self):
        self.authenticate()

        post = {
            'body': 'test_post'
        }

        response = self.client.post(self.create_post_url, post)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_post_not_authenticated(self):
        post = {
            'body': 'test_post'
        }

        response = self.client.post(self.create_post_url, post)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
