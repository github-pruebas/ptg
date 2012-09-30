from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.CharField(max_length=5)
    
    def __unicode__(self):
        return self.nombre