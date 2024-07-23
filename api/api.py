from rest_framework import viewsets, permissions
from .models import Colores, Publicaciones, Personalizaciones, Usuario, Carros
from .serializers import ColoresSerializer, PublicacionesSerializer, PersonalizacionesSerializer, UsuarioSerializer, CarrosSerializer

class ColoresViewSet(viewsets.ModelViewSet):
    queryset = Colores.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ColoresSerializer

class PublicacionesViewSet(viewsets.ModelViewSet):
    queryset = Publicaciones.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PublicacionesSerializer

class PersonalizacionesViewSet(viewsets.ModelViewSet):
    queryset = Personalizaciones.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PersonalizacionesSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UsuarioSerializer

class CarrosViewSet(viewsets.ModelViewSet):
    queryset = Carros.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CarrosSerializer
