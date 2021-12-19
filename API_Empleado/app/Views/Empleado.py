from app.models import Empleado
from app.serializers import EmpleadoSerializer
from rest_framework import viewsets

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset=Empleado.objects.all()
    serializer_class=EmpleadoSerializer