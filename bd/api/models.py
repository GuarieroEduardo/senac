from django.db import models

# Create your models here.
class Autores(models.Model):
    id_autor = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)

    def __str__(self):
        return self.nome

class Livros(models.Model):
    id_livro = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, null=False, blank=False)
    ano_publicado = models.DateField(null=True, blank=True)
    id_autor = models.ForeignKey(Autores, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo