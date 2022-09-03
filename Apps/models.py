from django.db import models

class Linea_telefonica(models.Model):
    
    Numero_celular = models.IntegerField(unique=True)
    Ex_compañia = models.CharField(max_length=33)

class Cliente (models.Model):
    Nombre_cliente = models.CharField(max_length=33)
    Email_cliente =models.EmailField(unique=True)
    Dni_cliente = models.IntegerField(unique=True)

class Empleado (models.Model):
    Nombre_empleado = models.CharField(max_length=33)
    Dni_empleado = models.IntegerField(unique=True)