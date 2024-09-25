from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.

from .forms import CustomUserCreateForm

class Register(CreateView):
    form_class = CustomUserCreateForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')