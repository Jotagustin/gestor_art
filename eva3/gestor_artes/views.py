from django.shortcuts import render
from .models import Colaboraciones, Proyecto, Artistas, Usuario, Rol, Historial

def registrar_historial(request, descripcion, tabla_afectada):
    """Registra una acción en el historial de auditoría"""
    try:
        if request.session.get('usuario'):
            from datetime import datetime
            usuario_obj = Usuario.objects.filter(username=request.session['usuario']).first()
            if usuario_obj:
                Historial.objects.create(
                    usuario=usuario_obj,
                    descripcion_historial=descripcion,
                    tabla_afectada_historial=tabla_afectada,
                    fecha_hora_historial=datetime.now()
                )
    except Exception as e:
        print(f"Error al registrar historial: {e}")

def verificar_sesion(request):

    if not request.session.get('usuario'):
        return render(request, 'gestor_artes/login.html', {
            'mensaje': 'Debes iniciar sesión para acceder a esta página'
        })
    return None

def verificar_rol_operador(request):

    auth_check = verificar_sesion(request)
    if auth_check:
        return auth_check
    
    if request.session.get('rol') == 'ADMIN':
        return render(request, 'gestor_artes/login.html', {
            'mensaje': 'Acceso denegado: Los administradores deben usar el Panel Admin'
        })
    return None


def mostrarLogin(request):
    return render(request, 'gestor_artes/login.html')

def mostrarFormCrearCuenta(request):
    return render(request, 'gestor_artes/form_crear_cuenta.html')

def validar_usuario(request):
    try:
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        if not username or not password:
            return render(request, 'gestor_artes/login.html', {'mensaje': 'Faltan credenciales'})

        usuario = Usuario.objects.filter(username=username, password=password).first()

        if usuario:
            request.session['usuario'] = usuario.username
            request.session['rol'] = usuario.rolname.upper()

            # Registrar inicio de sesión en historial
            registrar_historial(request, f"Inicio de sesión - Usuario {usuario.username} con rol {usuario.rolname}", "Usuario")

            rolActual = (usuario.rolname).upper()
            if rolActual == 'ARTISTA':
                return render(request, 'gestor_artes/menu_operador.html', {'mensaje': f'Bienvenido {usuario.username}'})
            if rolActual == 'ADMIN':
                return render(request, 'gestor_artes/menu_admin.html', {'mensaje': f'Bienvenido {usuario.username}'})
            return render(request, 'gestor_artes/login.html', {'mensaje': 'Rol no reconocido'})

        return render(request, 'gestor_artes/login.html', {'r2': 'Error De Usuario o Contraseña'})

    except Exception as error:
        print('validar_usuario fallo:', error)
        return render(request, 'gestor_artes/login.html', {'mensaje': 'Error interno'})

def iniciar_sesion(request):
    if request.method == "POST":
        return validar_usuario(request)
    return render(request, 'gestor_artes/login.html')

def crear_cuenta(request):
    username = request.POST['username']
    password = request.POST['password']
    Usu = Usuario(username=username, password=password, rolname=Rol.ARTISTA)
    Usu.save()
    

    try:
        from datetime import datetime
        admin_user = Usuario.objects.filter(rolname='ADMIN').first()
        if admin_user:
            Historial.objects.create(
                usuario=admin_user,
                descripcion_historial=f"Nueva cuenta creada para usuario: {username}",
                tabla_afectada_historial="Usuario",
                fecha_hora_historial=datetime.now()
            )
    except Exception as e:
        print(f"Error al registrar creación de cuenta: {e}")
    
    mensaje = 'Cuenta creada exitosamente'
    return render(request, 'gestor_artes/login.html', {'mensaje': mensaje})

def cerrarSesion(request):
    try:
        # Registrar cierre de sesión antes de eliminar la sesión
        if request.session.get('usuario'):
            registrar_historial(request, f"Cierre de sesión - Usuario {request.session['usuario']}", "Usuario")
        
        del request.session['usuario']
        del request.session['rol']
    except Exception:
        pass
    return render(request, 'gestor_artes/login.html', {'mensaje': 'Sesión cerrada'})

def mostrarMenuAdmin(request):
    auth_check = verificar_sesion(request)
    if auth_check:
        return auth_check
    
    if request.session.get('rol') != 'ADMIN':
        return render(request, 'gestor_artes/login.html', {
            'mensaje': 'Acceso denegado: Solo los administradores pueden acceder a esta sección'
        })
    
    return render(request, 'gestor_artes/menu_admin.html')

def mostrarMenuOperador(request):
    auth_check = verificar_rol_operador(request)
    if auth_check:
        return auth_check
    return render(request, 'gestor_artes/menu_operador.html')

def mostrarListarColaboraciones(request):
    auth_check = verificar_rol_operador(request)
    if auth_check:
        return auth_check
    colaboraciones = Colaboraciones.objects.all()
    datos = {'colaboraciones': colaboraciones}
    return render(request, 'gestor_artes/listar_colaboraciones.html', datos)

def mostrarFormRegistrarColaboracion(request):
    auth_check = verificar_rol_operador(request)
    if auth_check:
        return auth_check
    return render(request, 'gestor_artes/form_registrar_colaboraciones.html', {
        'proyectos': [],
        'artistas': [],
    })

def registrarColaboracion(request):
    auth_check = verificar_sesion(request)
    if auth_check:
        return auth_check
    return render(request, 'gestor_artes/listar_colaboraciones.html', {
        'colaboraciones': [],
        'proyectos': [],
    })

def mostrarFormActualizarColaboracion(request):
    auth_check = verificar_sesion(request)
    if auth_check:
        return auth_check
    return render(request, 'gestor_artes/form_actualizar_colaboraciones.html', {
        'colaboracion': None,
        'proyectos': [],
        'artistas': [],
    })

def actualizarColaboracion(request):
    auth_check = verificar_sesion(request)
    if auth_check:
        return auth_check
    return render(request, 'gestor_artes/listar_colaboraciones.html', {
        'colaboraciones': [],
        'proyectos': [],
    })

def eliminarColaboracion(request):
    auth_check = verificar_sesion(request)
    if auth_check:
        return auth_check
    return render(request, 'gestor_artes/listar_colaboraciones.html', {
        'colaboraciones': [],
        'proyectos': [],
    })

def mostrarListarHistorial(request):
    try:
        auth_check = verificar_sesion(request)
        if auth_check:
            return auth_check
        
        # Validación de rol - solo ADMIN puede ver historial
        if request.session.get('rol') != 'ADMIN':
            return render(request, 'gestor_artes/login.html', {
                'mensaje': 'Acceso denegado: Solo los administradores pueden acceder a esta sección'
            })
        
        # Obtener historial ordenado por fecha descendente
        historial = Historial.objects.select_related('usuario').all().order_by('-fecha_hora_historial')
        
        datos = {
            'usuario_actual': request.session.get('usuario'),
            'historial': historial
        }
        
        return render(request, 'gestor_artes/listar_historial.html', datos)
        
    except Exception as e:
        print(f"Error al obtener historial: {e}")
        return render(request, 'gestor_artes/login.html', {'mensaje': 'Error al obtener historial'})

def mostrarFormCrearProyecto(request):
    auth_check = verificar_rol_operador(request)
    if auth_check:
        return auth_check
    return render(request, 'gestor_artes/form_crear_proyecto.html')

def registrarProyecto(request):
    auth_check = verificar_rol_operador(request)
    if auth_check:
        return auth_check
    if request.method != 'POST':
        return render(request, 'gestor_artes/form_crear_proyecto.html', {'mensaje': 'Método no permitido'})

    titulo = request.POST.get('titulo', '').strip()
    if not titulo:
        return render(request, 'gestor_artes/form_crear_proyecto.html', {'mensaje': 'El título es obligatorio'})

    p = Proyecto(titulo=titulo)
    p.save()
    
    # Registrar creación de proyecto en historial
    registrar_historial(request, f"Proyecto creado: {titulo}", "Proyecto")
    
    return render(request, 'gestor_artes/menu_operador.html', {'mensaje': f'Proyecto "{titulo}" creado'})

def filtroEmpieza(request):
    auth_check = verificar_sesion(request)
    if auth_check:
        return auth_check
    filtro = request.POST['txtfil']
    colabs = Colaboraciones.objects.filter(proyecto__titulo__istartswith=filtro)
    datos = {'colaboraciones': colabs}
    return render(request, 'gestor_artes/listar_colaboraciones.html', datos)

def filtroContenga(request):
    auth_check = verificar_sesion(request)
    if auth_check:
        return auth_check
    filtro = request.POST['txtfil']
    colabs = Colaboraciones.objects.filter(artista__nombre__icontains=filtro)
    datos = {'colaboraciones': colabs}
    return render(request, 'gestor_artes/listar_colaboraciones.html', datos)

def filtroEntre(request):
    auth_check = verificar_sesion(request)
    if auth_check:
        return auth_check
    val1 = request.POST['txtval1']
    val2 = request.POST['txtval2']
    colabs = Colaboraciones.objects.filter(valor__range=(val1, val2))
    datos = {'colaboraciones': colabs}
    return render(request, 'gestor_artes/listar_colaboraciones.html', datos)