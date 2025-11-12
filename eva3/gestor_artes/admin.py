from django.contrib import admin
from .models import Proyecto, Artistas, Colaboraciones, Usuario

class ProyectoAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo']
    search_fields = ['titulo']

admin.site.register(Proyecto, ProyectoAdmin)

class ArtistasAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    search_fields = ['nombre']

admin.site.register(Artistas, ArtistasAdmin)

class ColaboracionesAdmin(admin.ModelAdmin):
    list_display = ['id', 'proyecto', 'artista', 'valor', 'fecha_registro']
    list_filter = ['proyecto']
    search_fields = ['fecha_registro']

admin.site.register(Colaboraciones, ColaboracionesAdmin)

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'password', 'rolname']
    search_fields = ['username']

admin.site.register(Usuario, UsuarioAdmin)