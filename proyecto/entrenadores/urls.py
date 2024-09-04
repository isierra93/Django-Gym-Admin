from django.urls import path

from . import views

app_name = 'entrenadores'

urlpatterns = [
    path('', views.index, name='index'),
    path('entrenador/list', views.entrenador_list, name='entrenador_list'),
    path('entrenador/create', views.entrenador_create, name='entrenador_create'),
]