#from django.shortcuts import render
from app.models import Documento
from app.serializers import DocumentoSerializer

from rest_framework import viewsets
# Create your views here.
class DocumentoViewSet(viewsets.ModelViewSet):
    queryset=Documento.objects.all()
    serializer_class=DocumentoSerializer