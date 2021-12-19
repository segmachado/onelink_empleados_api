from app.models import Area
from app.serializers import AreaSerializer
from rest_framework import viewsets

class AreaViewSet(viewsets.ModelViewSet):
    queryset=Area.objects.all()
    serializer_class=AreaSerializer