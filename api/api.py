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


import base64
from django.core.files.base import ContentFile
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Publicaciones
from .serializers import PublicacionesSerializer


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

    def create(self, request, *args, **kwargs):
        data = request.data.copy()  # Hacer una copia mutable de los datos

        # Decodificar la imagen base64
        if "imagen" in data:
            format, imgstr = data["imagen"].split(";base64,")
            ext = format.split("/")[-1]
            data["imagen"] = ContentFile(base64.b64decode(imgstr), name=f"image.{ext}")

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


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
