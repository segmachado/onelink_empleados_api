from app.models import Documento
from app.serializers import DocumentoSerializer
from rest_framework import viewsets

class DocumentoViewSet(viewsets.ModelViewSet):
    queryset=Documento.objects.all()
    serializer_class=DocumentoSerializer