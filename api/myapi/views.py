from django.shortcuts import render

# Create your views here.

# Importa os decoradores do Django REST Framework para definir rotas baseadas em funções
from rest_framework.decorators import api_view  
# Importa a classe Response para retornar respostas HTTP formatadas
from rest_framework.response import Response  
# Importa os códigos de status HTTP predefinidos (ex: HTTP_201_CREATED, HTTP_400_BAD_REQUEST)
from rest_framework import status  
# Importa o modelo Funcionario, que representa a tabela no banco de dados
from .models import Funcionario  
# Importa o serializer que converte objetos Funcionario para JSON e vice-versa
from .serializers import FuncionarioSerializer  

# -------------------------------
# 📌 LISTAR TODOS OS FUNCIONÁRIOS
# -------------------------------
# Define uma API que aceita apenas requisições GET
@api_view(['GET'])  
def listar_funcionarios(request):  
    """
    Retorna a lista de todos os funcionários cadastrados no banco de dados.
    """
    # Obtém todos os funcionários cadastrados
    funcionarios = Funcionario.objects.all()  
    # Serializa os funcionários para transformar os dados em JSON
    serializer = FuncionarioSerializer(funcionarios, many=True)  
    # Retorna a lista de funcionários no formato JSON
    return Response(serializer.data)  

# -------------------------------
# 📌 CADASTRAR UM NOVO FUNCIONÁRIO
# -------------------------------
# Define uma API que aceita apenas requisições POST
@api_view(['POST'])  
def cadastrar_funcionario(request):  
    """
    Cadastra um novo funcionário no banco de dados.
    """
    # Converte os dados recebidos no corpo da requisição para um objeto Funcionario
    serializer = FuncionarioSerializer(data=request.data)  
    # Verifica se os dados fornecidos são válidos de acordo com as regras do serializer
    if serializer.is_valid():  
        # Salva o novo funcionário no banco de dados
        serializer.save()  
        # Retorna os dados do funcionário criado com o status 201 (Created)
        return Response(serializer.data, status=status.HTTP_201_CREATED)  
    # Se os dados forem inválidos, retorna os erros e o status 400 (Bad Request)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

# -------------------------------
# 📌 OBTER UM FUNCIONÁRIO POR ID
# -------------------------------
# Define uma API que aceita apenas requisições GET
@api_view(['GET'])  
def obter_funcionario(request, id):  
    """
    Busca um funcionário pelo ID e retorna seus dados.
    """
    try:  
        # Tenta buscar o funcionário pelo ID fornecido
        funcionario = Funcionario.objects.get(id=id)  
        # Serializa os dados do funcionário encontrado
        serializer = FuncionarioSerializer(funcionario)  
        # Retorna os dados do funcionário no formato JSON
        return Response(serializer.data)  
    except Funcionario.DoesNotExist:  
        # Se o funcionário não for encontrado, retorna uma mensagem de erro e status 404 (Not Found)
        return Response({"erro": "Funcionário não encontrado"}, status=status.HTTP_404_NOT_FOUND)  

