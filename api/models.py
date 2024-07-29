from django.db import models


class Colores(models.Model):
    codigo_hex = models.CharField(
        max_length=7, default=""
    )  # Cambiado a 7 para códigos hexadecimales de color estándar

    def __str__(self):
        return self.codigo_hex


class Publicaciones(models.Model):
    nombre_usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField(default="")
    me_gusta = models.PositiveIntegerField(default=0)
    no_me_gusta = models.PositiveIntegerField(default=0)
    imagen = models.ImageField(
        upload_to="imagenes_publicaciones/", null=True, blank=True
    )

    def __str__(self):
        return f"{self.nombre_usuario.nombre_usuario}: {self.descripcion}"


class Personalizaciones(models.Model):
    nombre_usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)
    nombre_personalizacion = models.CharField(max_length=50, default="")
    numero_personalizacion = models.CharField(max_length=50, default="")
    imagen = models.ImageField(
        upload_to="personalizaciones/", null=True, blank=True
    )  # Nuevo campo para la imagen

    def __str__(self):
        return self.nombre_personalizacion


class Carros(models.Model):
    nombre_modelo = models.CharField(max_length=50, default="")
    url_modelo_3d = models.URLField(
        max_length=200, default=""
    )  # Usado URLField en lugar de CharField

    def __str__(self):
        return self.nombre_modelo


class Usuario(models.Model):
    nombre_usuario = models.CharField(
        max_length=50, unique=True, default=""
    )  # Añadido unique=True para nombre de usuario
    primer_nombre = models.CharField(max_length=50, default="")
    segundo_nombre = models.CharField(
        max_length=50, blank=True, default=""
    )  # Permitir en blanco
    primero_apellido = models.CharField(max_length=50, default="")
    segundo_apellido = models.CharField(
        max_length=50, blank=True, default=""
    )  # Permitir en blanco
    correo = models.EmailField(
        max_length=254, unique=True, default=""
    )  # Usado EmailField en lugar de CharField
    contrasena = models.CharField(
        max_length=128, default=""
    )  # Aumentado el max_length para contraseñas

    def __str__(self):
        return self.nombre_usuario


class Comentario(models.Model):
    publicacion = models.ForeignKey(
        "Publicaciones", on_delete=models.CASCADE, related_name="comentarios"
    )
    usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)
    texto = models.TextField()
    fecha_comentario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.usuario.nombre_usuario} en {self.publicacion.descripcion}"
