from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=11)
    email = models.EmailField(max_length=100)
    curso = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nome} - {self.data_nascimento} - {self.email} - {self.curso}"

