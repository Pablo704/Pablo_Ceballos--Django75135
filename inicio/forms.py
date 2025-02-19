from django import forms

class AgregarCarrera(forms.Form):
    nombre = forms.CharField(max_length=20)
    fecha = forms.CharField(max_length=20)
    circuito = forms.CharField(max_length=20)
    
class AgregarPiloto(forms.Form):
    nombre = forms.CharField(max_length=20)
    equipo = forms.CharField(max_length=20)
    puntos = forms.CharField(max_length=20)
    
class Buscar(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)
    equipo = forms.CharField(max_length=20, required=False)
