from django.shortcuts import render
from rest_framework.response import Response
from .faker_generator.faker_gen import UserGen, ItemGen
from rest_framework.decorators import api_view
import json


@api_view(['GET'])
def user_gen(request):
    body =json.loads(request.body)
    n = body['number']
    accounts = UserGen.gen(n)
    return Response(accounts)

@api_view(['GET'])
def item_gen(request):
    return Response({'itens': ItemGen.gen()})