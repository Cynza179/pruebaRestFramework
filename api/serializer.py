from rest_framework import serializers
from .models import Profesor

class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profesor
        fields='__all__'   #>(dni,) Se usa para serializar todos los campos de mi modelo#
        
#model y fields son obligatorios#