import os, sys
from typing import Type
from .igen_product import IGenProduct
from faker import Faker
import json

fake = Faker()

class UserGenProduct(IGenProduct):
    def __init__(self, count: int = 0):
         self.count = count

    def gen(self):
        new_accounts = []
        for i in range(0, self.count):
                first_name = fake.first_name()
                last_name = fake.last_name()
                fake_user = {
                            'username': '%s%s%s' % (first_name,last_name,fake.random_number(digits=2, fix_len=False)),
                            'first_name': first_name,
                            'end_name': last_name,
                            'phone': fake.phone_number(),
                            'email': f'{first_name}{last_name}{fake.random_number()}@{fake.free_email_domain()}',
                            'password': '123',
                            'ip': {'ipv4': fake.ipv4(), 'ipv6': fake.ipv6()}
                        }
                new_accounts.append(fake_user)
        return new_accounts