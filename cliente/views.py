from django.shortcuts import render
from cliente.models import DadosCliente


def home(request):
    return render(request, 'index.html', {});
