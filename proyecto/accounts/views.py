from django.views.generic import CreateView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.

from .forms import CustomUserCreateForm, UserProfileForm

class Register(CreateView):
    form_class = CustomUserCreateForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')

class Profile(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'accounts/profile.html'
    success_url = reverse_lazy('core:index')

    def get_object(self):
        return self.request.user