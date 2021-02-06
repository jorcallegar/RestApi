#Import the Hero model
#Import the REST Framework serializer
#Create a new class that links the Hero with its serializer

# serializers.py
from rest_framework import serializers

from .models import Hero

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('name', 'alias')