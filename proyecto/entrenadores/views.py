from django.views.generic import View, ListView, CreateView, DeleteView, UpdateView
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Entrenador, Clase
from .forms import EntrenadorForm, ClaseForm

# Create your views here.
""" Entrenadores """
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
    success_url = reverse_lazy('entrenadores:entrenador_list')

class EntrenadorDelete(DeleteView):
    model = Entrenador
    success_url = reverse_lazy('entrenadores:entrenador_list')

class EntrenadorUpdate(UpdateView):
    model = Entrenador
    form_class = EntrenadorForm
    success_url = reverse_lazy('entrenadores:entrenador_list')

""" Clases """

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

class ClaseDelete(DeleteView):
    model = Clase
    success_url = reverse_lazy('entrenadores:clase_list')

class ClaseUpdate(UpdateView):
    model = Clase
    form_class = ClaseForm
    success_url = reverse_lazy('entrenadores:clase_list')