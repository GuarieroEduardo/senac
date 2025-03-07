from rest_framework import viewsets
from ..models import Autores, Livros
from ..serializers import AutoresSerializer, LivrosSerializer

class AutoresViewSet(viewsets.ModelViewSet):
    queryset = Autores.objects.all()
    serializer_class = AutoresSerializer

class LivrosViewSet(viewsets.ModelViewSet):
    queryset = Livros.objects.all()
    serializer_class = LivrosSerializer



