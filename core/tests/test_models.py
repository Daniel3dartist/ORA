from django.test import TestCase
from ..models import MyUser, Item
from fake_gen.faker_generator.faker_gen import FakerGen
from fake_gen.faker_generator.generators.usergen import UserGen
import json

fake = FakerGen

class TestModels(TestCase):
#class TestModels:
    def setUp(self):
        
        fuser = fake.generate(UserGen(count=1)) # Fake User Generation
        fuser = fuser[0]
        user = MyUser.objects.create(username=fuser['username'],
                                     first_name=fuser['first_name'],
                                     end_name= fuser["end_name"],
                                     phone=str(fuser['phone']),
                                     email=fuser['email'],
                                     password=fuser['password'],
                                     ip=json.dumps(fuser['ip']))
#        print(MyUser.objects.all())
        item = Item.objects.create()

    def test_models(self):
        print(MyUser.objects.all())
        assert len(MyUser.objects.all()) > 0
