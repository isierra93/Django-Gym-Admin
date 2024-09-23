from django.views.generic import View, ListView, CreateView, DeleteView, UpdateView
from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Cliente
from .forms import ClienteForm

# Create your views here.

class IndexView(View):
    def get(self, request):
        return render( request, 'clientes/index.html')

class ClienteList(ListView):
    model = Cliente

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            return queryset.filter(nombre__icontains=q)
        return queryset

class ClienteCreate(CreateView):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy('clientes:cliente_list')

class ClienteDelete(DeleteView):
    model = Cliente
    success_url = reverse_lazy('clientes:cliente_list')

class ClienteUpdate(UpdateView):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy('clientes:cliente_list')