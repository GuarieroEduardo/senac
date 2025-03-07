from django.urls import path, include

# # biblioteca rest_framework
from rest_framework.routers import DefaultRouter
from .views.api_views import AutoresViewSet, LivrosViewSet
from .views.web_views import Livraria


router = DefaultRouter()    

router.register('autores', AutoresViewSet)
router.register('livros', LivrosViewSet)


urlpatterns = [
    path('api/', include(router.urls)),  
    path('livraria/', Livraria, name='livraria'),
]

