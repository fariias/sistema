from django.db import models
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    sexos = ((1,'Masculino'),(2,'Feminino'))
    sexo = models.IntegerField(choices=sexos,default=1)
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
    codigo = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100) 
    def __str__(self):
        return str(self.codigo)

class Contrato(models.Model):
    cliente = models.ForeignKey("Cliente")
    rastreador = models.ForeignKey("Rastreador")
    dia5=5
    dia10=10
    dia15=15
    vencimentos = ((dia5,'Todo dia 5'),(dia10,'Todo dia 10'),(dia15,'Todo dia 15'),)
    vencimento = models.IntegerField(choices=vencimentos)
    avista = 'AV'
    parcelado = 'PC'
    pagamentos = (
        (avista,'Em Dinheiro'),
        (parcelado,'Parcelado'),
        )
    pagamento = models.CharField(max_length=2,choices=pagamentos,default=avista)
    veiculo = models.CharField(max_length=100)
    modelo = models.CharField(max_length=50)
    cor = models.CharField(max_length=25)
    marca = models.CharField(max_length=50)
    ano = models.CharField(max_length=20)
    placa = models.CharField(max_length=20)
