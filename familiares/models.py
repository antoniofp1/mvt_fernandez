from django.db import models

class pr_familia(models.Model):
    nombre = models.CharField(max_length=64)
    fecha_nac = models.DateField()
    dni = models.IntegerField()


