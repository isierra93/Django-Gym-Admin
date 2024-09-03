from django.urls import path

from . import views

app_name = 'clientes'

urlpatterns = [
    path('', views.index, name='index' ),
    path('cliente/list', views.cliente_list , name='cliente_list'),
    path('cliente/create', views.cliente_create, name='cliente_create')
]