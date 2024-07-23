from rest_framework import serializers
from .models import Colores, Publicaciones, Personalizaciones, Usuario, Carros

class ColoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colores
        fields = '__all__'

class PublicacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicaciones
        fields = '__all__'

class PersonalizacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personalizaciones
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class CarrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carros
        fields = '__all__'
