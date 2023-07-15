from rest_framework import viewsets          #viewsets sirve para visualar contenido json#from django.shortcuts import render se borra por no tener contenido html#
from .serializer import ProfesorSerializer
from .models import Profesor

# Create your views here.
class ProfesorViewSet(viewsets.ModelViewSet):
    queryset=Profesor.objects.all()
    serializer_class=ProfesorSerializer
    