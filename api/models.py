from django.db import models

# Create your models here.
class Colores(models.Model):
     codigo_hex = models.CharField(max_length=50,default='')

class Publicaciones(models.Model):
     nombre_usuario = models.CharField(max_length=50,default='')
     fecha_publicacion = models.CharField(max_length=50,default='')
     descripcion = models.CharField(max_length=50,default='')
     me_gusta = models.CharField(max_length=50,default='')
     no_me_gusta = models.CharField(max_length=50,default='')
     comentarios = models.CharField(max_length=50,default='')

class Personalizaciones(models.Model):
     nombre_usuario = models.CharField(max_length=50,default='')
     nombre_personalizacion = models.CharField(max_length=50,default='')
     numero_personalizacion = models.CharField(max_length=50,default='')     

class Usuario(models.Model):
     nombre_usuario = models.CharField(max_length=50,default='')
     primer_nombre = models.CharField(max_length=50,default='')
     segundo_nombre = models.CharField(max_length=50,default='')
     primero_apellido = models.CharField(max_length=50,default='')
     segundo_apellido = models.CharField(max_length=50,default='')
     correo = models.CharField(max_length=50,default='')
     contrasena = models.CharField(max_length=50,default='')

class Carros(models.Model):
     nombre_modelo = models.CharField(max_length=50,default='')
     url_modelo_3d = models.CharField(max_length=50,default='')
     