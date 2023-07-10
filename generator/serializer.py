from rest_framework import serializers 
from .models import link


class LinkSerializers( serializers.ModelSerializer):
    class Meta:
        model = link
        fields = '__all__'