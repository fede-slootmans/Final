from django.db import models
from django.utils import timezone

class Contacto(models.Model):
    nombre_apellido = models.CharField(max_length=120)
    email = models.EmailField()
    asunto = models.CharField(max_length=50)
    mensaje = models.TextField()
    fecha = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.nombre_apellido