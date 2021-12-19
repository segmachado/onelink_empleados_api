from app.models import Documento,Area,SubArea,Empleado
from rest_framework import serializers

class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Documento
        fields = ['id','nombreDocumento','formato']

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Area
        fields=['id','nombreArea','activa']

class SubAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model=SubArea
        fields=['id','nombreSubArea','activa','area']

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Empleado
        fields=['id','documento','numDocumento','nombres','apellidos','subarea','fecha_creacion']