from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'entrenadores'

urlpatterns = [
    path('', login_required(views.IndexView.as_view()), name='index'),
    path('entrenador/list', login_required(views.EntrenadorList.as_view()), name='entrenador_list'),
    path('entrenador/create', login_required(views.EntrenadorCreate.as_view()), name='entrenador_create'),
    path('entrenadores/delete/<int:pk>', login_required(views.EntrenadorDelete.as_view()), name='entrenador_delete'),
    path('entrenadores/update/<int:pk>', login_required(views.EntrenadorUpdate.as_view()), name='entrenador_update'),
    path('clase/list', login_required(views.ClaseList.as_view()), name='clase_list'),
    path('clase/create', login_required(views.ClaseCreate.as_view()), name='clase_create'),
    path('clase/delete/<int:pk>', login_required(views.ClaseDelete.as_view()), name='clase_delete'),
    path('clase/update/<int:pk>', login_required(views.ClaseUpdate.as_view()), name='clase_update'),
]