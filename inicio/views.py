from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


from datetime import datetime
from inicio.models import Carrera, Piloto
from inicio.forms import AgregarCarrera, AgregarPiloto, Buscar, ModificarPiloto, ModificarCarrera


@login_required
def inicio(request,):
    hora_actual = datetime.now()
    carreras = Carrera.objects.all()
    return render(request, 'inicio.html', {'hora': hora_actual, 'carreras': carreras})

def eliminar_carrera(request, carrera_id):
    carrera = Carrera.objects.get(id=carrera_id)
    carrera.delete()
    return redirect('inicio')

def modificar_carrera(request, carrera_id):
    carrera = Carrera.objects.get(id=carrera_id)
    
    if request.method == "POST":
        formulario = ModificarCarrera(request.POST, instance=carrera)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    else:
        formulario = ModificarCarrera(instance=carrera)

    return render(request, 'modificar.html', {'formulario': formulario})

@login_required
def agregar_carrera(request):
    print(request.GET)
    print(request.POST)
    
    formulario = AgregarCarrera()
    
    if request.method == "POST":
        formulario = AgregarCarrera(request.POST)
        if formulario.is_valid():
           nombre = formulario.cleaned_data.get('nombre')
           fecha = formulario.cleaned_data.get('fecha')
           circuito = formulario.cleaned_data.get('circuito')
           
           carrera = Carrera(nombre = nombre, fecha = fecha, circuito = circuito)
           carrera.save()
           
    
    return render(request, 'agregar_carrera.html', {'formulario' : formulario}, )


@login_required
def agregar_piloto(request):
    
    print(request.GET)
    print(request.POST)
    
    formulario = AgregarPiloto()
    
    if request.method == "POST":
        formulario = AgregarPiloto(request.POST)
        if formulario.is_valid():
           nombre = formulario.cleaned_data.get('nombre')
           equipo = formulario.cleaned_data.get('equipo')
           puntos = formulario.cleaned_data.get('puntos')
           
           piloto = Piloto (nombre = nombre, equipo = equipo, puntos = puntos)
           piloto.save()
           
           return redirect('listado_de_puntos')
           
    return render(request, 'agregar_piloto.html', {'formulario' : formulario})
@login_required
def listado_de_puntos(request):
    pilotos = Piloto.objects.all()

    formulario = Buscar(request.GET)
    if formulario.is_valid():
        equipo_a_buscar = formulario.cleaned_data.get('equipo')
        nombre_a_buscar = formulario.cleaned_data.get('nombre')
        pilotos = Piloto.objects.filter(equipo__icontains = equipo_a_buscar, nombre__icontains = nombre_a_buscar)
    
    return render(request, 'listado_de_puntos.html', {'pilotos' : pilotos, 'formulario' : formulario})

@login_required
def ver_piloto(request, piloto_id):
    piloto = Piloto.objects.get(id=piloto_id)
    return render(request, 'ver_piloto.html', {'piloto': piloto})

# Vistas Comunes
# def eliminar_piloto(request, piloto_id):
#     piloto = Piloto.objects.get(id=piloto_id)
#     piloto.delete()
#     return redirect('listado_de_puntos')
# def modificar_piloto(request, piloto_id):
    
#     piloto = Piloto.objects.get(id=piloto_id)

#     if request.method == "POST":
#         formulario = ModificarPiloto(request.POST, instance=piloto)
#         if formulario.is_valid():
#             formulario.save()
#             return redirect('listado_de_puntos')
#     else:
#         formulario = ModificarPiloto(instance=piloto)
#     return render(request, 'modificar.html', {'formulario': formulario})

#CBV

class ModificarPilotoVista(LoginRequiredMixin, UpdateView):
    model = Piloto
    template_name = "CBV/modificar_piloto.html"
    form_class = ModificarPiloto
    success_url = reverse_lazy("listado_de_puntos")

    def form_valid(self, form):
        
        if self.request.FILES.get('imagen'):
            form.instance.imagen = self.request.FILES['imagen']  
        
        self.object = form.save() 
        return super().form_valid(form)

class EliminarPilotoVista(LoginRequiredMixin, DeleteView):
    model = Piloto
    template_name = "CBV/eliminar_piloto.html"
    success_url = reverse_lazy('listado_de_puntos')
