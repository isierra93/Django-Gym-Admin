from django.views.generic import View, ListView, CreateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Entrenador, Clase
from .forms import EntrenadorForm, ClaseForm

# Create your views here.

class IndexView(View):
    def get(self, request):
        return render(request, 'entrenadores/index.html')

class EntrenadorList(ListView):
    model = Entrenador

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            return queryset.filter(nombre__icontains=q)
        return queryset
    
class EntrenadorCreate(CreateView):
    model = Entrenador
    form_class = EntrenadorForm
    reverse_lazy = 'entrenadores:entrenador_list'

class ClaseList(ListView):
    model = Clase

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            return queryset.filter(nombre__icontains=q)
        return queryset

class ClaseCreate(CreateView):
    model = Clase
    form_class = ClaseForm
    success_url = reverse_lazy('entrenadores:clase_list')