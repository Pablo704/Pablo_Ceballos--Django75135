from django.db import models

class Carrera(models.Model):
    nombre = models.CharField(max_length=20)
    fecha = models.CharField(max_length=20)
    circuito = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.nombre} {self.fecha} {self.circuito}"
    
class Piloto(models.Model):
    nombre = models.CharField(max_length=20)
    equipo = models.CharField(max_length=20)
    puntos = models.IntegerField()
    fecha_creacion = models.DateField(null=True, blank=True)
    imagen = models.ImageField(upload_to="pilotos/", null=True, blank=True)

    
    def __str__(self):
        return f"{self.nombre} - {self.equipo} - {self.puntos}"
    
