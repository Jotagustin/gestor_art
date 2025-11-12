from django.db import models

class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)

class Artistas(models.Model):
    nombre = models.CharField(max_length=100)

class Colaboraciones(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='proyectos_colab')
    artista = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='artistas_colab')
    valor = models.IntegerField()
    fecha_registro = models.CharField(max_length=100)

class Rol(models.Model):
    rolname = models.CharField(max_length=100)

class Usuario(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    rolname = models.ForeignKey(Rol, on_delete=models.CASCADE)
