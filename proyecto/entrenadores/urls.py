from django.urls import path

from . import views

app_name = 'entrenadores'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('entrenador/list', views.EntrenadorList.as_view(), name='entrenador_list'),
    path('entrenador/create', views.EntrenadorCreate.as_view(), name='entrenador_create'),
    path('clase/list', views.ClaseList.as_view(), name='clase_list'),
    path('clase/create', views.ClaseCreate.as_view(), name='clase_create'),
]