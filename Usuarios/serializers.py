from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'es_mentor', 'es_admin']


class EntradaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entrada
        fields = ['id', 'titulo', 'contenido', 'fecha', 'autor']