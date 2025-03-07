from inicio.views import inicio, agregar_carrera, agregar_piloto, listado_de_puntos, ver_piloto, eliminar_carrera, modificar_carrera, ModificarPilotoVista, EliminarPilotoVista
from django.urls import path

urlpatterns = [
    path('', inicio, name='inicio'),
    path('agregar-carrera', agregar_carrera, name='agregar_carrera'),
    path('agregar-piloto', agregar_piloto, name='agregar_piloto'),
    path('listado-de-puntos/', listado_de_puntos, name='listado_de_puntos' ),
    path('ver-piloto/<int:piloto_id>/', ver_piloto, name='ver_piloto'),
    #CBV
    path('eliminar-piloto/<int:pk>/', EliminarPilotoVista.as_view(), name='eliminar_piloto'),
    path('modificar_piloto/<int:pk>/', ModificarPilotoVista.as_view(), name='modificar_piloto'), 
    #Vista comunes
    path('eliminar-carrera/<int:carrera_id>/', eliminar_carrera, name='eliminar_carrera'),
    path('modificar-carrera/<int:carrera_id>/', modificar_carrera, name='modificar_carrera')
]
