from django.urls import path, include

# biblioteca rest_framework
from rest_framework.routers import DefaultRouter
from .views import FuncionarioViewSet

router = DefaultRouter()    

router.register('funcionarios', FuncionarioViewSet)


urlpatterns = [
    path('', include(router.urls)),  
      
]

