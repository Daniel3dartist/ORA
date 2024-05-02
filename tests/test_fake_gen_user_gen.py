from django.test import TestCase
from fake_gen.faker_generator.faker_gen import FakerGen
from fake_gen.faker_generator.generators.usergen import UserGen


#class TestFakeGen(TestCase): # Django manage.py test
class TestFakeGen: # Pytest
    def test_gen(self):
        fake = FakerGen
        user_gen = UserGen(count=2)
        result = fake.generate(user_gen)
        print(result)
        print(type(result))
        assert type(result) == list


if __name__ == "__main__":
    TestFakeGen.test_gen()