from django import forms
from .models import Medicamento, AsignacionSuministro
class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = ['categoria', 'nombre', 'clave', 'descripcion', 'fecha_caducidad', 'cantidad', 'status']

class AsignacionSuministroForm(forms.ModelForm):
    class Meta:
        model = AsignacionSuministro
        fields = ['asignado_a', 'medicamento', 'cantidad']