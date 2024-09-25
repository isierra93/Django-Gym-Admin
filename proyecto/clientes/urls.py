from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'clientes'

urlpatterns = [
    path('', login_required(views.IndexView.as_view()), name='index' ),
    path('cliente/list', login_required(views.ClienteList.as_view()) , name='cliente_list'),
    path('cliente/create', login_required(views.ClienteCreate.as_view()), name='cliente_create'),
    path('cliente/delete/<int:pk>', login_required(views.ClienteDelete.as_view()), name='cliente_delete'),
    path('cliente/update/<int:pk>', login_required(views.ClienteUpdate.as_view()), name='cliente_update')
]