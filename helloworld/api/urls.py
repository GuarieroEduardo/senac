from django.urls import path

from .views import(listar_funcionarios, cadastrar_funcionario, obter_funcionario)

urlpatterns = [
    path('funcionarios/', listar_funcionarios, name='listar_funcionario'),
    path('funcionarios/cadastrar/', cadastrar_funcionario, name='cadastrar_funcionario'),
    path('obter/<int:id>', obter_funcionario,  name='obter_funcionario'),
]

