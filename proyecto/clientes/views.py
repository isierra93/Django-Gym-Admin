from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm

# Create your views here.

def index(request):
    return render(request, 'clientes/index.html')

def cliente_list(request):
    q = request.GET.get('q')
    if q:
        query = Cliente.objects.filter(nombre__icontains=q)
    else:
        query = Cliente.objects.all()
    context = {'object_list': query}
    return render(request, 'clientes/cliente_list.html', context)

def cliente_create(request):
    if request.method == 'GET':
        form = ClienteForm()

    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes:cliente_list')
    return render(request, 'clientes/cliente_form.html', {'form': form})