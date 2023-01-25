from django.db import models

# Create your models here.
class estudiantes(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    

class profesor(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    profesion= models.CharField(max_length=30)

class entregable(models.Model):
    nombre=models.CharField(max_length=30)
    fechaDeEntrega=models.DateField()
    entregado=models.BooleanField()

class curso(models.Model):
    nombre= models.CharField(max_length=30)
    comision= models.IntegerField()
