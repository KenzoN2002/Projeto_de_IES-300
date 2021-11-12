from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Prato, Bebida, Sobremesa, Comanda

def index(request):
    num_prato = Pratos.objects.count()
    num_sobremesa = Sobremesa.objects.count()
    num_bebida =  Bebida.object.count()
    num_comanda = Comanda.objects.all().count()

    context = {
        'num_comanda': num_comanda,
        'num_prato': num_prato,
        'num_sobremesa': num_sobremesa,
        'num_bebida': num_bebida,
        'num_comanda': num_comanda,

    }
    return render(request, 'index.html', context=context)

#Visualizações do Prato

class PratoCreate(CreateView):
    model = Prato
    fields = ['nome']

class PratoUpdate(UpdateView):
    model = Prato
    fields = '__all__' 


class PratoDelete(DeleteView):
    model = Prato
    success_url = reverse_lazy('pratos')

class PratoListView(generic.ListView):
    model = Prato
    paginate_by = 10

class PratoDetailView(generic.DetailView):
    """Generic class-based detail view for an author."""
    model = Prato

#Visualização de Sobremesa

class SobremesaCreate(CreateView):
    model = Sobremesa
    fields = ['nome']

class SobremesaUpdate(UpdateView):
    model = Sobremesa
    fields = '__all__'

class SobremesaDelete(DeleteView):
    model = Sobremesa
    success_url = reverse_lazy('sobremesas')

class SobremesaListView(generic.ListView):
    model = Sobremesa
    paginate_by = 10

class SobremesaDetailView(generic.DetailView):
    model = Sobremesa

#Visualizações das Bebidas
class BebidaCreate(CreateView):
    model = Bebida
    fields = ['nome']

class BebidaUpdate(UpdateView):
    model = Bebida
    fields = '__all__'

class BebidaDelete(DeleteView):
    model = Bebida
    success_url = reverse_lazy('bebidas')

class BebidaListView(generic.ListView):
    model = Bebida
    paginate_by = 10

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
