from django.contrib import admin
from django.urls import path
from gestor_artes import views 

urlpatterns = [
    path('admin/', admin.site.urls),

    # Login / Session
    path('', views.mostrarLogin, name='mostrar_login'),
    path('iniciar_sesion', views.iniciarSesion, name='iniciar_sesion'),
    path('cerrar_sesion', views.cerrarSesion, name='cerrar_sesion'),

    # Menús
    path('menu_admin', views.mostrarMenuAdmin, name='mostrar_menu_admin'),
    path('menu_operador', views.mostrarMenuOperador, name='mostrar_menu_operador'),

    # Colaboraciones (Operador)
    path('listar_colaboraciones', views.mostrarListarColaboraciones, name='mostrar_listar_colaboraciones'),
    path('form_registrar_colaboracion', views.mostrarFormRegistrarColaboracion, name='mostrar_form_registrar_colaboracion'),
    path('registrar_colaboracion', views.registrarColaboracion, name='registrar_colaboracion'),
    path('form_actualizar_colaboracion', views.mostrarFormActualizarColaboracion, name='mostrar_form_actualizar_colaboracion'),
    path('actualizar_colaboracion', views.actualizarColaboracion, name='actualizar_colaboracion'),
    path('eliminar_colaboracion', views.eliminarColaboracion, name='eliminar_colaboracion'),

    # Historial (Admin)
    path('listar_historial', views.mostrarListarHistorial, name='mostrar_listar_historial'),
]
