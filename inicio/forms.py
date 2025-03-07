from django import forms
from inicio.models import Piloto, Carrera 

class AgregarCarrera(forms.Form):
    nombre = forms.CharField(max_length=20)
    fecha = forms.CharField(max_length=20)
    circuito = forms.CharField(max_length=20)
    
class AgregarPiloto(forms.Form):
    nombre = forms.CharField(max_length=20)
    equipo = forms.CharField(max_length=20)
    puntos = forms.CharField(max_length=20)
    fecha_creacion = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Fecha de Creación")
    imagen = forms.ImageField(required=False, label="Imagen (opcional)")
    
class Buscar(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)
    equipo = forms.CharField(max_length=20, required=False)
    
class ModificarPiloto(forms.ModelForm):
    fecha_creacion = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Fecha de Creación")
    class Meta:
        model = Piloto
        fields = "__all__"

class ModificarCarrera(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = "__all__"
