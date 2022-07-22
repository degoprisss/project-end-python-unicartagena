from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Inventory
class SerializerInventary(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Inventory