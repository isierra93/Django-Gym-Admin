from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Empleados(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='empleado')
    avatar = models.ImageField(upload_to='avatares', blank=True, null=True)

    def __str__(self):
        return self.usuario.username
    
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'