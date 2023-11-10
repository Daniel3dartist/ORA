from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient, APIRequestFactory
import json

factory = APIRequestFactory

class TestView(TestCase):
    def test_status_code_200(self):
        result = factory.get(reverse('user_gen'), data=json.dumps({'number':2}))
        print('Status CODE: ', result)
        assert result.status_code == 200