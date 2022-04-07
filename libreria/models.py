from django.db import models

class Editorial(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.TextField(max_length=150)

    def __str__(self):
        return self.nombre


# Create your models here.
class Libro(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre= models.TextField(max_length=150)
    num_paginas = models.IntegerField()
    fecha_publicacion = models.DateField()
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.nombre, self.num_paginas, self.fecha_publicacion




