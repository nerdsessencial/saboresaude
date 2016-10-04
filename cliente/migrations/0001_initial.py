# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-04 16:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cardapio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, null=True, verbose_name='Nome da Op\xe7\xe3o')),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Descri\xe7\xe3o')),
            ],
        ),
        migrations.CreateModel(
            name='DadosCliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_fantasia', models.CharField(max_length=100, verbose_name='Nome Fantasia')),
                ('razao_social', models.CharField(max_length=100, verbose_name='Raz\xe3o Social')),
                ('cnpj', models.CharField(max_length=14, verbose_name='CNPJ')),
                ('telefone1_empresa', models.CharField(max_length=11, verbose_name='Telefone 1')),
                ('telefone2_empresa', models.CharField(max_length=11, verbose_name='Telefone 2')),
                ('endereco', models.CharField(max_length=100, null=True, verbose_name='Endere\xe7o')),
                ('situacao', models.BooleanField(default=False, verbose_name='Situa\xe7\xe3o')),
            ],
        ),
        migrations.CreateModel(
            name='Responsavel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('celular', models.CharField(max_length=11)),
                ('telefone', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='TipoRefeicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=1)),
                ('preco', models.DecimalField(blank=True, decimal_places=2, max_digits=5, verbose_name='Pre\xe7o')),
                ('descricao', models.CharField(max_length=200, verbose_name='Descri\xe7\xe3o')),
            ],
        ),
        migrations.AddField(
            model_name='dadoscliente',
            name='responsavel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.Responsavel', verbose_name='Respons\xe1vel'),
        ),
        migrations.AddField(
            model_name='dadoscliente',
            name='tipo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.TipoRefeicao', verbose_name='Tipo Refei\xe7\xe3o'),
        ),
        migrations.AddField(
            model_name='cardapio',
            name='tipo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.TipoRefeicao', verbose_name='Tipo Refei\xe7\xe3o'),
        ),
    ]
