from django.shortcuts import render 
from ..models import Aluno  

def home(request):
    alunos = Aluno.objects.all()
    return render(request, 'home.html', {'alunos': alunos})

def CriarAluno(request):
    return render(request, 'criar_aluno.html')
