from django.shortcuts import render
from rest_framework.response import Response
from .faker_generator.faker_gen import FakerGen
from rest_framework.decorators import api_view
import json


@api_view(['GET'])
def user_gen(request):
    body =json.loads(request.body)
    n = body['number']
    fake = FakerGen(usercount=n)
    accounts = fake.usergen()
    return Response(accounts)

@api_view(['GET'])
def item_gen(request):
    fake = FakerGen()
    items = fake.itemgen()
    return Response({'itens': items})