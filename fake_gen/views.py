from django.shortcuts import render
from rest_framework.response import Response
from .faker_generator.faker_gen import FakerGen
from rest_framework.decorators import api_view
from .faker_generator.generators.usergen import UserGen
import json
from django.http import HttpResponse


@api_view(['GET'])
def user_gen(request):
    """Fake user generator view
    """
    n = int(request.GET['number'])
    fake = FakerGen
    accounts = fake.generate(UserGen(count=n))
    return Response(data=json.dumps(accounts))


@api_view(['GET'])
def item_gen(request):
    return Response('None')
'''    fake = FakerGen()
    items = fake.itemgen()
    return Response({'itens': items})
'''