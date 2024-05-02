from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient, APIRequestFactory
import json

factory = APIClient()

class TestView(TestCase):
    def test_status_code_200(self):
        result = factory.get(reverse('user_gen'), data={'number':2}, format=json)
        print('Status CODE: ', result.status_code)
        assert result.status_code == 200
