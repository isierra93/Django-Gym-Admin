from django.urls import path

from . import views

app_name = 'clientes'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index' ),
    path('cliente/list', views.ClienteList.as_view() , name='cliente_list'),
    path('cliente/create', views.ClienteCreate.as_view(), name='cliente_create')
]