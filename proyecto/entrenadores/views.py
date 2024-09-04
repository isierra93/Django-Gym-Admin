from django.shortcuts import render, redirect
from .models import Entrenador, Clase
from .forms import EntrenadorForm, ClaseForm

# Create your views here.

def index(request):
    return render(request, 'entrenadores/index.html')

def entrenador_list(request):
    q = request.GET.get('q')
    if q:
        query = Entrenador.objects.filter(nombre__icontains=q)
    else:
        query = Entrenador.objects.all()
    context = {'object_list': query}
    return render(request, 'entrenadores/entrenador_list.html', context)

def entrenador_create(request):
    if request.method == 'GET':
        form = EntrenadorForm()

    if request.method == 'POST':
        form = EntrenadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('entrenadores:entrenador_list')
    return render(request, 'entrenadores/entrenador_form.html', {'form': form} )
