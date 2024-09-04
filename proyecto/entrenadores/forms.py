from django import forms

from .models import Entrenador, Clase

class EntrenadorForm(forms.ModelForm):
    class Meta:
        model = Entrenador
        fields = '__all__'

class ClaseForm(forms.ModelForm):
    class Meta:
        model = Clase
        fields = '__all__'
        widgets = {'horario' : forms.TimeInput(attrs={'type': 'time'})}