from django.db import models


# Create your models here.
class Cliente(models.Model):
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class Telefone(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    ddd = models.IntegerField()
    numero = models.CharField('Número', max_length=9)

    def __str__(self):
        return '(' + str(self.ddd) + ') ' + str(self.numero)


class Modalidade(models.Model):
    sigla = models.CharField(max_length=10)
    descricao = models.CharField('Descrição', max_length=100)

    def __str__(self):
        return self.sigla


class Indice(models.Model):
    sigla = models.CharField(max_length=10)
    descricao = models.CharField('Descrição', max_length=100)

    def __str__(self):
        return self.sigla


class Aliquota(models.Model):
    indice = models.ForeignKey(Indice, on_delete=models.CASCADE, verbose_name='Índice')
    vigencia = models.DateField('Data Inicial de Vigência')
    aliquota = models.DecimalField('Taxa % a.a.', max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.vigencia) + ' - ' + str(self.aliquota)


class Programa(models.Model):
    indice = models.ForeignKey(Indice, on_delete=models.RESTRICT, verbose_name='Índice')
    modalidade = models.ForeignKey(Modalidade, on_delete=models.RESTRICT)
    descricao = models.CharField('Descrição', max_length=100)

    def __str__(self):
        return self.descricao


class Proposta(models.Model):
    programa = models.ForeignKey(Programa, on_delete=models.RESTRICT)
    cliente = models.ForeignKey(Cliente, on_delete=models.RESTRICT)
    contrato = models.CharField(max_length=20)
    data_criacao = models.DateField('Data de Criação')
    valor_principal = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    numero_de_parcelas = models.IntegerField('Número de Parcelas', default=0)

    def __str__(self):
        return self.contrato


class Parcela(models.Model):
    proposta = models.ForeignKey(Proposta, on_delete=models.CASCADE)
    numero = models.IntegerField('Número')
    vencimento = models.DateField('Data de Vencimento')
    valor = models.DecimalField(max_digits=18, decimal_places=2)

    def __str__(self):
        return str(self.numero) + ' - ' + str(self.vencimento) + ' - R$ ' + str(self.valor)


class Pagamento(models.Model):
    parcela = models.ForeignKey(Parcela, on_delete=models.CASCADE)
    data_pagamento = models.DateField('Data de Pagamento')
    valor = models.DecimalField(max_digits=18, decimal_places=2)

    def __str__(self):
        return str(self.data_pagamento) + ' - R$ ' + str(self.valor)

