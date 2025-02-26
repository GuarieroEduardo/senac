from django.db import models
# Create your models here.

class Funcionario(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    sobrenome = models.CharField(max_length=255, null=False, blank=False)
    cpf = models.CharField(max_length=14, null=False, blank=False)
    tempo_de_servico = models.IntegerField(default=0, null=False, blank=False)
    renumeracao = models.DecimalField(max_digits=8, decimal_places=2, default=0, null=False, blank=False)

    def __str__(self):
        return f"{self.name} {self.sobrenome}"
    
class Produto(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    quantidade_estoque = models.IntegerField(default=0, null=False, blank=False)
    valor_unitario = models.DecimalField(max_digits=8, decimal_places=2, default=0, null=False, blank=False)

    def __str__(self):
        return self.nome
    


