from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Entrenador)
admin.site.register(models.Clase)