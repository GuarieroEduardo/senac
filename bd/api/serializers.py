from rest_framework import serializers
from .models import Autores, Livros

class AutoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autores
        fields = '__all__'

class LivrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livros
        fields = '__all__'

