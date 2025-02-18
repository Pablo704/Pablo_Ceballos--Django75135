from inicio.views import inicio, saludo
from django.urls import path
urlpatterns = [
    path('', inicio, name='inicio'),
    path('saludo/<str:nombre>/', saludo, name='saludo')
]
