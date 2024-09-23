from django.urls import path

from . import views

app_name = 'entrenadores'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('entrenador/list', views.EntrenadorList.as_view(), name='entrenador_list'),
    path('entrenador/create', views.EntrenadorCreate.as_view(), name='entrenador_create'),
    path('entrenadores/delete/<int:pk>', views.EntrenadorDelete.as_view(), name='entrenador_delete'),
    path('entrenadores/update/<int:pk>', views.EntrenadorUpdate.as_view(), name='entrenador_update'),
    path('clase/list', views.ClaseList.as_view(), name='clase_list'),
    path('clase/create', views.ClaseCreate.as_view(), name='clase_create'),
    path('clase/delete/<int:pk>', views.ClaseDelete.as_view(), name='clase_delete'),
    path('clase/update/<int:pk>', views.ClaseUpdate.as_view(), name='clase_update'),
]