from rest_framework import serializers
from .models import *


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class TelefoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telefone
        fields = '__all__'

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'
