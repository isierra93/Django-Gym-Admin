from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('register', views.Register.as_view() , name='register'),
    path('profile', views.Profile.as_view(), name='profile')
]

##Si aca despues creo un path que sea de PROFILE me redirecciona automaticamente sin tocar mi settings.py