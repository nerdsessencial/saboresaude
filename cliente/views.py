from django.shortcuts import render
from cliente.models import DadosCliente
from django.http import HttpResponse
from .models import Pedido
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import PedidoForm


def home(request):
    return render(request, 'index.html', {});

@login_required(login_url="login/")
def lista_pedidos(request):
   pedidos = Pedido.objects.all()
   return render(request, 'pedidos.html', {'pedidos': pedidos})

def novo_pedido(request):
    form = PedidoForm()
    return render(request, 'editar_pedido.html', {'form': form})
