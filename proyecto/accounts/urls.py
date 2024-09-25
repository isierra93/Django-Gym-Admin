from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'accounts'

urlpatterns = [
    path('login', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout', LogoutView.as_view(template_name='accounts/logout.html'), name='logout')
]

##Si aca despues creo un path que sea de PROFILE me redirecciona automaticamente sin tocar mi settings.py