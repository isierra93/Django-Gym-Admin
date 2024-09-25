from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about', views.AboutView.as_view(), name='about')
]