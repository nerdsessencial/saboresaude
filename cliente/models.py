# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

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
        return ' '.join(self.numero)
    
    

class Cardapio(models.Model):
    nome = models.CharField(max_length=50, null=True, verbose_name='Nome da Opção')
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição')
    tipo = models.ForeignKey(TipoRefeicao, null=True, verbose_name="Tipo Refeição")

    class meta:
        app_label='Responsáveis'

    def __str__(self):
        return ' '.join([
            self.nome,
            self.descricao,
            self.tipo.numero
        ])

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
    tipo = models.ForeignKey(TipoRefeicao, null=True, verbose_name="Tipo Refeição")
    

    def __str__(self):
        return ''.join([
            self.nome_fantasia,
            self.razao_social,
            self.cnpj,
            self.telefone1_empresa,
            self.telefone2_empresa,
            self.responsavel.nome,
        ])

    class meta:
        app_label='Dados Clientes'

class Pedido(models.Model):
    dados_cliente = models.ForeignKey("DadosCliente", verbose_name="Dados Cliente")
    quantidade = models.IntegerField(blank=True, null=False, verbose_name='Quanto')

    def __str__(self):
        return ''.join([
            self.dados_cliente.id,
            self.quantidade,
        ])

    class meta:
        app_label='Pedido'