from django.urls import path

from . import views

app_name = 'clientes'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index' ),
    path('cliente/list', views.ClienteList.as_view() , name='cliente_list'),
    path('cliente/create', views.ClienteCreate.as_view(), name='cliente_create'),
    path('cliente/delete/<int:pk>', views.ClienteDelete.as_view(), name='cliente_delete'),
    path('cliente/update/<int:pk>', views.ClienteUpdate.as_view(), name='cliente_update')
]