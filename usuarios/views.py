from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as django_login
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from usuarios.forms import MiFormularioDeCreacion, MiFormularioDeEdicion
from usuarios.models import InfoExtra
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method == "POST":
        formulario =  AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            
            django_login(request, usuario)
            
            InfoExtra.objects.get_or_create(user=usuario)
            
            return redirect('inicio')
    else:
        formulario = AuthenticationForm( )
        
    return render(request, 'usuarios/login.html', {'formulario' : formulario})

def registro(request):
    
    if request.method == "POST":
        formulario =  MiFormularioDeCreacion(request.POST)
        if formulario.is_valid():
            formulario.save()
            
            return redirect('login')
    else:
        formulario = MiFormularioDeCreacion( )
        
    return render(request, 'usuarios/registro.html', {'formulario' : formulario})

@login_required
def ver_perfil(request):
    return render(request, 'usuarios/ver_perfil.html', {'user': request.user})

def editar_perfil(request):
    
    info_extra = request.user.infoextra
    
    if request.method == "POST":
        formulario =  MiFormularioDeEdicion(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            
            if formulario.cleaned_data.get('avatar'):
                info_extra.avatar = formulario.cleaned_data.get('avatar')
                
            info_extra.save()
            
            formulario.save()
            
            return redirect('inicio')
    else:
        formulario = MiFormularioDeEdicion(instance=request.user, user=request.user, initial={'avatar': info_extra.avatar})
        
    return render(request, 'usuarios/editar_perfil.html', {'formulario' : formulario})

class CambioPassword(PasswordChangeView):
    template_name = 'usuarios/cambio_pass.html'
    success_url = reverse_lazy('inicio')