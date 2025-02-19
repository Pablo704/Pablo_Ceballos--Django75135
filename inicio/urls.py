from inicio.views import inicio, agregar_carrera, agregar_piloto, listado_de_puntos
from django.urls import path

urlpatterns = [
    path('', inicio, name='inicio'),
    path('agregar-carrera', agregar_carrera, name='agregar_carrera'),
    path('agregar-piloto', agregar_piloto, name='agregar_piloto'),
    path('listado-de-puntos/', listado_de_puntos, name='listado_de_puntos' )
]
