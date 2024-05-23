from django.shortcuts import render
from rest_framework.response import Response
from .faker_generator.faker_gen import FakerGen
from rest_framework.decorators import api_view
from .faker_generator.generators.usergen import UserGen
import json
from django.http import HttpResponse


@api_view(['GET'])
def user_gen(request):
    """Fake user generator
    Parameters:
        count: int
    """
    try:
        n = int(request.GET["number"])
    except:
        n=1
    fake = FakerGen
    accounts = fake.generate(UserGen(count=n))
    return Response(accounts)


@api_view(['GET'])
def item_gen(request):
    return Response('None')
'''    fake = FakerGen()
    items = fake.itemgen()
    return Response({'itens': items})
'''