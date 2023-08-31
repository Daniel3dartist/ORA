import os, sys
from faker import Faker
import json



fake = Faker()

class UserGen():
    def gen():
        fake_user = {
            'name': fake.name(),
            'email': fake.free_email(),
            'password': '123'
        }
        return fake_user
    
class ItemGen():
    def gen():
        try:
            with open('shop_itens.json', 'r') as file:
                j = json.load(file)
                return j
        except:
            return 'ERRO on read shop_itens.json file'