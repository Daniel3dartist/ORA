from .models import Item
#from django.contrib.auth.models import User
from rest_framework import serializers


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'desc']