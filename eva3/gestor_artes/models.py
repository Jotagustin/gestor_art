from django.db import models

class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)

class Artistas(models.Model):
    nombre = models.CharField(max_length=100)

class Colaboraciones(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='proyectos_colab')
    artista = models.ForeignKey(Artistas, on_delete=models.CASCADE, related_name='artistas_colab')
    valor = models.IntegerField()
    fecha_registro = models.CharField(max_length=100)

class Rol(models.TextChoices):
    ADMIN = 'ADMIN', 'Admin'
    OPERADOR = 'OPERADOR', 'Operador'
    ARTISTA = 'ARTISTA', 'Artista'

class Usuario(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    rolname = models.CharField(max_length=20, choices=Rol.choices, default=Rol.OPERADOR)

class Historial(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    descripcion_historial = models.TextField(max_length=200)
    tabla_afectada_historial = models.TextField(max_length=100)
    fecha_hora_historial = models.DateTimeField()
