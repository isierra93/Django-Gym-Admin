from django.db import models

# Create your models here.
class Cliente(models.Model):
    """Clientes registrados en sistema"""
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField(unique=True)
    telefono = models.IntegerField()
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f'{self.apellido} , {self.nombre}'
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'