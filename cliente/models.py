# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from sabor import settings
from datetime import datetime, timedelta

# Create your models here.

class Responsavel(models.Model):
    nome = models.CharField(max_length=100)
    celular = models.CharField(max_length=11)
    telefone = models.CharField(max_length=11)

    class meta:
        app_label='Responsáveis'

    def __str__(self):
        return self.nome
    
    

class TipoRefeicao(models.Model):
     numero = models.CharField(max_length=1, null=False)
     preco = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=False, verbose_name='Preço')
     descricao = models.CharField(max_length=200, null=False, verbose_name='Descrição')

     class meta:
        app_label='Tipos de Refeição'

     def __str__(self):
        return self.numero
    
    

class Cardapio(models.Model):
    nome = models.CharField(max_length=50, null=True, verbose_name='Nome da Opção')
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição')
    tipo = models.ForeignKey(TipoRefeicao, null=True, verbose_name="Tipo Refeição")

    class meta:
        app_label='Responsáveis'

    def __str__(self):
        return self.nome

    class meta:
        app_label='Cardápio'
     

class DadosCliente(models.Model):
    nome_fantasia = models.CharField(max_length=100, null=False, verbose_name='Nome Fantasia')
    razao_social = models.CharField(max_length=100, null=False, verbose_name='Razão Social')
    cnpj = models.CharField(max_length=14, null=False, verbose_name='CNPJ')
    telefone1_empresa = models.CharField(max_length=11, null=False, verbose_name='Telefone 1')
    telefone2_empresa = models.CharField(max_length=11, verbose_name='Telefone 2')
    endereco = models.CharField(max_length=100, null=True, verbose_name='Endereço')
    situacao = models.BooleanField(default=False, null=False, verbose_name='Situação')

    responsavel = models.ForeignKey(Responsavel, verbose_name="Responsável")
    

    def __str__(self):
        return self.nome_fantasia

class Pedido(models.Model):
    empresa = models.ForeignKey(DadosCliente, null=True, verbose_name="Empresa")
    tipo_refeicao = models.ForeignKey(TipoRefeicao, null=True, verbose_name="Tipo Refeição")
    data_pedido = models.DateTimeField(default=datetime.now() ,verbose_name="Data Pedido")
    quantidade_refeicoes = models.IntegerField(blank=True, null=False, verbose_name='Qtd. Refeições')
    status = models.IntegerField(blank=True, null=True, default=1, verbose_name='Status do Pedido')

    def __str__(self):
        return self.empresa.nome_fantasia