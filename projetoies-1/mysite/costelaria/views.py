from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Prato, Bebida, Sobremesa, Comanda


def index(request):
    num_comanda = ComandaInstance.objects.all().count()
    return render(
        request,
        'index.html',
        context={'num_comanda': num_comanda},
    )

#Visualizações do Prato

class PratoDetailView(generic.DetailView):
    """Generic class-based detail view for an author."""
    model = Prato

#Visualização de Sobremesa

class SobremesaDetailView(generic.DetailView):
    model = Sobremesa

#Visualizações das Bebidas

class BebidaDetailView(generic.DetailView):
    model = Bebida

#Visualizações das comandas
class ComandaCreate(CreateView):
    model = Comanda
    fields = ['mesa', 'prato', 'sobremesa', 'bebida']


class ComandaUpdate(UpdateView):
    model = Comanda
    fields = ['mesa', 'prato', 'sobremesa', 'bebida']


class ComandaDelete(DeleteView):
    model = Comanda
    success_url = reverse_lazy('Comandas')

class ComandaListView(generic.ListView):
    model = Comanda
    paginate_by = 10

class ComandaDetailView(generic.DetailView):
    model = Comanda
