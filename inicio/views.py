from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from inicio.models import Carrera, Piloto
from inicio.forms import AgregarCarrera, AgregarPiloto, Buscar



def inicio(request,):
    hora_actual = datetime.now()
    return render(request, 'inicio.html', {'hora': hora_actual})


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
    
    return render(request, 'agregar_carrera.html', {'formulario' : formulario})



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

def listado_de_puntos(request):
    pilotos = Piloto.objects.all()
    formulario = Buscar(request.GET)
    if formulario.is_valid():
        equipo_a_buscar = formulario.cleaned_data.get('equipo')
        nombre_a_buscar = formulario.cleaned_data.get('nombre')
        pilotos = Piloto.objects.filter(equipo__icontains = equipo_a_buscar, nombre__icontains = nombre_a_buscar)
    
    return render(request, 'listado_de_puntos.html', {'pilotos' : pilotos, 'formulario' : formulario})