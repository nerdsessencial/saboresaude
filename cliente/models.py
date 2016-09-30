# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Responsavel(models.Model):
    nome = models.CharField(max_length=100)
    celular = models.CharField(max_length=11)
    telefone = models.CharField(max_length=11)

    def __str__(self):
        return ''.join([
            self.nome,
            self.celular,
            self.telefone,
        ])

class DadosCliente(models.Model):
    nome_fantasia = models.CharField(max_length=100)
    razao_social = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14)
    telefone1_empresa = models.CharField(max_length=11)
    telefone2_empresa = models.CharField(max_length=11)
    responsavel = models.ForeignKey(Responsavel, verbose_name="Responsáveis")

    def __str__(self):
        return ''.join([
            self.nome_fantasia,
            self.razao_social,
            self.cnpj,
            self.telefone1_empresa,
            self.telefone2_empresa,
            self.responsavel.nome,
        ])


