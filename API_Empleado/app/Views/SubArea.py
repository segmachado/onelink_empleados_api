from app.models import SubArea
from app.serializers import SubAreaSerializer
from rest_framework import viewsets

class SubAreaViewSet(viewsets.ModelViewSet):
    queryset=SubArea.objects.all()
    serializer_class=SubAreaSerializer