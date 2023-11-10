from rest_framework import status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .models import Item
from .serializers import ItemSerializer

import json

"""
Debit:
    Abstract the code in view
"""

@api_view(['GET'])
def items(request):
    if request.method == "GET":
        items_count = int(request.GET['number'])
        if items_count == None:
            itens = Item.objects.all()
            serializer = ItemSerializer(itens, many = True)
            return Response('passou aqui') #Response(serializer.data)

@api_view(['POST'])
def sing_up(request):
    _user = request.body['user']
    _email = request.body['email']
    _password = request.body['password']
    is_valid = '' # Need to add validator
    if is_valid == False:
        return Response('not valid')
    else:
        try:
            User.objects.create_user(username=_user.lower(), 
                                     email=str(_email).lower(), 
                                     password=_password)
            
            return Response(f'User create successfuly!')
        except:
            return Response(f'[ERRO] Erro to create user {_user}.\nUser already exists')

@api_view(['POST', 'GET', "PUT", "DELETE"])
def users(request):
    if request.method == 'POST':
        pass
    elif request.method == "GET":
        pass
    elif request.method == "PUT":
        pass
    elif request.method == "DELETE":
        pass

"""
@api_view(['GET'])
def users(request):
    content = request.GET
    _user = content['username']
#    _email = content['email']
    print(_user)
    data = {'is_available': False,
            'notify': '',
            }
    try:
        if User.objects.get(username=_user.lower()):
            data['is_available'] = False
            data['notify'] = f'{_user} is already in use. \nPlease try another username.'
            return Response(data)


    except:
        data['is_available'] = True
        return Response(data)
"""

#@permission_classes([IsAuthenticated])
#@staff_member_required
#@authentication_classes([BasicAuthentication])
"""
@api_view(['POST'])
def post_item(request):
    if request.method == "POST":
        print('POST')
        data = JSONParser().parse(request)
        serializer = ItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
"""