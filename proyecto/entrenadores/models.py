from django.db import models

# Create your models here.
class Entrenador(models.Model):
    """Entreadores registrados en el sistema con su tipo de especialidad"""
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nombre} - {self.especialidad}'
    
    class Meta:
        verbose_name = 'Entrenador'
        verbose_name_plural = 'Entrenadores'


class Clase(models.Model):
    nombre = models.CharField(max_length=100)
    entrenador = models.ForeignKey(Entrenador, on_delete=models.CASCADE)
    horario = models.TimeField()

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Clase'
        verbose_name_plural = 'Clases'