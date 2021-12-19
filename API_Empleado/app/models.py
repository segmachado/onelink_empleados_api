from django.db import models

class Area(models.Model):
    nombreArea=models.CharField(max_length=100)
    activa=models.BooleanField(default=True)

class SubArea(models.Model):
    nombreSubArea=models.CharField(max_length=100)
    area=models.ForeignKey(Area,null=False,blank=False,on_delete=models.CASCADE)
    activa=models.BooleanField(default=True)

class Documento(models.Model):
    nombreDocumento=models.CharField(max_length=100)
    formato=models.CharField(max_length=25)

class Empleado(models.Model):
    documento=models.ForeignKey(Documento,null=False,blank=False,on_delete=models.CASCADE)
    numDocumento=models.CharField(max_length=25)
    nombres=models.CharField(max_length=100)
    apellidos=models.CharField(max_length=100)
    subarea=models.ForeignKey(SubArea,null=False,blank=False,on_delete=models.CASCADE)
    fecha_creacion=models.DateTimeField(auto_now_add=True)