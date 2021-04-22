from django.db import models

class Telefone(models.Model):
    ddd = models.CharField(max_length=8)
    numero = models.CharField(max_length=16, unique=True)
    tipo = models.CharField(max_length=16)

    def __str__(self):
        return self.numero

class Email(models.Model):
    email = models.EmailField(max_length=254, unique=True)

    def __str__(self):
        return self.email

class Cliente(models.Model):
    nome = models.CharField(max_length=128)
    rg = models.CharField(max_length=16, unique=True)
    cpf = models.CharField(max_length=16, unique=True)
    data_nasc = models.DateField()
    sexo = models.CharField(max_length=128)
    telefone = models.OneToOneField(Telefone, on_delete=models.SET_NULL, blank=True, null=True)
    email = models.OneToOneField(Email, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.nome + '(' + self.cpf + ')'
