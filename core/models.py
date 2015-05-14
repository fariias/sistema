from django.db import models
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=100)
    nascimento = models.CharField(max_length=20)
    rg = models.IntegerField()
    cpf = models.IntegerField()
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    def __str__(self):
        return self.nome

class Consultor(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.IntegerField()

class Rastreador(models.Model):
    tipo = models.CharField(max_length=100) 
    

class Contrato(models.Model):
    cliente = models.ForeignKey("Cliente")
    consultor = models.ForeignKey("Consultor")
    rastreador = models.ForeignKey("Rastreador")
    vencimento = models.IntegerField()
    veiculo = models.CharField(max_length=100)
    modelo = models.CharField(max_length=50)
    cor = models.CharField(max_length=25)
    marca = models.CharField(max_length=50)
    ano = models.CharField(max_length=20)
    placa = models.CharField(max_length=20)
