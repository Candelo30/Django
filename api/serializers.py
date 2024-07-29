from rest_framework import serializers
from .models import (
    Colores,
    Publicaciones,
    Personalizaciones,
    Usuario,
    Carros,
    Comentario,
)


class ColoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colores
        fields = "__all__"


class PublicacionesSerializer(serializers.ModelSerializer):
    nombre_usuario = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all())
    nombre_usuario_display = serializers.SerializerMethodField()

    class Meta:
        model = Publicaciones
        fields = "__all__"

    def get_nombre_usuario_display(self, obj):
        return obj.nombre_usuario.nombre_usuario

    def validate(self, data):
        # Ejemplo de validación personalizada
        if "me_gusta" not in data or "no_me_gusta" not in data:
            raise serializers.ValidationError(
                "Los campos 'me_gusta' y 'no_me_gusta' son obligatorios."
            )
        return data


class PersonalizacionesSerializer(serializers.ModelSerializer):
    nombre_usuario = (
        serializers.StringRelatedField()
    )  # O usa UsuarioSerializer si deseas más detalles

    class Meta:
        model = Personalizaciones
        fields = "__all__"


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"

    def validate(self, data):
        # Ejemplo de validación personalizada
        if len(data.get("contrasena", "")) < 6:
            raise serializers.ValidationError(
                "La contraseña debe tener al menos 6 caracteres."
            )
        return data


class CarrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carros
        fields = "__all__"


class ComentarioSerializer(serializers.ModelSerializer):
    publicacion = (
        serializers.StringRelatedField()
    )  # O usa PublicacionesSerializer si deseas más detalles
    usuario = (
        serializers.StringRelatedField()
    )  # O usa UsuarioSerializer si deseas más detalles

    class Meta:
        model = Comentario
        fields = "__all__"
