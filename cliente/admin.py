# -*- coding: utf-8 -*-
from django.contrib import admin
from cliente.models import DadosCliente, Responsavel, TipoRefeicao, Cardapio, Pedido


class DadosClienteAdmin(admin.ModelAdmin):
    """
    Admin para o model DadosCliente
    """
    list_display = ('nome_fantasia', 'razao_social', 'cnpj', 'telefone1_empresa', 'telefone2_empresa', 'responsavel')
    list_filter = ['nome_fantasia', 'razao_social', 'responsavel']
    search_fields = ['nome_fantasia__razao_social']

class ResponsavelAdmin(admin.ModelAdmin):
    """
    Admin para o model Responsavel
    """
    list_display = ('nome', 'celular', 'telefone')
    list_filter = ['nome']
    search_fields = ['nome']

class TipoRefeicaoAdmin(admin.ModelAdmin):
    """
    Admin para o model TipoRefeicao
    """
    list_display = ('numero', 'preco', 'descricao')
    list_filter = ['numero']
    search_fields = ['numero__descricao']
    
class CardapioAdmin(admin.ModelAdmin):
    """
    Admin para o model Cardapio
    """
    list_display = ('nome', 'descricao', 'tipo')
    list_filter = ['nome']
    search_fields = ['nome__tipo']

class PedidoAdmin(admin.ModelAdmin):
    """
    Admin para o model Cardapio
    """
    list_display = ('dados_cliente', 'quantidade')
    list_filter = ['dados_cliente']
    search_fields = ['dados_cliente']

admin.site.register(DadosCliente, DadosClienteAdmin)
admin.site.register(Responsavel, ResponsavelAdmin)
admin.site.register(TipoRefeicao, TipoRefeicaoAdmin)
admin.site.register(Cardapio, CardapioAdmin)
admin.site.register(Pedido, PedidoAdmin)
