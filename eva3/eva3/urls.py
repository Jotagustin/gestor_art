from django.contrib import admin
from django.urls import path
from gestor_artes import views as gestor_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Login / Session
    path('', gestor_views.mostrarLogin, name='mostrar_login'),
    path('iniciar_sesion', gestor_views.iniciarSesion, name='iniciar_sesion'),
    path('cerrar_sesion', gestor_views.cerrarSesion, name='cerrar_sesion'),

    # Menús
    path('menu_admin', gestor_views.mostrarMenuAdmin, name='mostrar_menu_admin'),
    path('menu_operador', gestor_views.mostrarMenuOperador, name='mostrar_menu_operador'),

    # Colaboraciones (Operador)
    path('listar_colaboraciones', gestor_views.mostrarListarColaboraciones, name='mostrar_listar_colaboraciones'),
    path('form_registrar_colaboracion', gestor_views.mostrarFormRegistrarColaboracion, name='mostrar_form_registrar_colaboracion'),
    path('registrar_colaboracion', gestor_views.registrarColaboracion, name='registrar_colaboracion'),
    path('form_actualizar_colaboracion', gestor_views.mostrarFormActualizarColaboracion, name='mostrar_form_actualizar_colaboracion'),
    path('actualizar_colaboracion', gestor_views.actualizarColaboracion, name='actualizar_colaboracion'),
    path('eliminar_colaboracion', gestor_views.eliminarColaboracion, name='eliminar_colaboracion'),

    # Historial (Admin)
    path('listar_historial', gestor_views.mostrarListarHistorial, name='mostrar_listar_historial'),
]
