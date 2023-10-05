import os, sys
from faker import Faker
import json


fake = Faker()

class UserGen:
    def gen(n):
        new_accounts = []
        for i in range(0, n):
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