from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def inicio(request):
    return render(request, 'inicio.html')

def saludo (request, nombre):
    hora_actual = datetime.now()
    return render(request, 'saludo.html', {'hora': hora_actual, 'nombre': nombre})

