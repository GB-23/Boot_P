from django.db import models
from django.contrib.auth.models import User


class Pessoa(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuarios")
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    rg = models.CharField(max_length=20)
    endereco = models.CharField(max_length=255)
    bairro = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50) 

    def __str__(self):
        return f"{self.nome} ({self.cpf})"
    
    
class Endereco(models.Model):
    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
        related_name='enderecos'
    )
    rua = models.CharField(max_length=255)
    numero = models.CharField(max_length=20)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=9)

    def __str__(self):
        return f"{self.rua}, {self.numero} – {self.bairro}"