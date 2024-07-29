from rest_framework import viewsets, permissions
from .models import (
    Colores,
    Publicaciones,
    Personalizaciones,
    Usuario,
    Carros,
    Comentario,
)
from .serializers import (
    ColoresSerializer,
    PublicacionesSerializer,
    PersonalizacionesSerializer,
    UsuarioSerializer,
    CarrosSerializer,
    ComentarioSerializer,
)


class ColoresViewSet(viewsets.ModelViewSet):
    queryset = Colores.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ColoresSerializer


class PublicacionesViewSet(viewsets.ModelViewSet):
    queryset = Publicaciones.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PublicacionesSerializer

    def get_queryset(self):
        queryset = Publicaciones.objects.all()
        usuario_id = self.request.query_params.get("nombre_usuario_id", None)
        if usuario_id is not None:
            queryset = queryset.filter(nombre_usuario_id=usuario_id)
        return queryset


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


class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ComentarioSerializer
