from django.test import TestCase
from ..faker_generator.faker_gen import FakerGen
from ..faker_generator.generators.usergen import UserGen

fakegen = FakerGen

#class TestFakeGen(TestCase): # Django manage.py test
class TestFakeGen: # Pytest
    def test_gen(self):
        result = fakegen.generate(UserGen(count=2))#usergen)
        print(result)
        print(type(result))
        assert type(result) == list


if __name__ == "__main__":
    TestFakeGen.test_gen()