from django.shortcuts import render
from .models import Colaboraciones, Proyecto, Artistas, Usuario, Rol

def verificar_sesion(request):

    if not request.session.get('usuario'):
        return render(request, 'gestor_artes/login.html', {
            'mensaje': 'Debes iniciar sesión para acceder a esta página'
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

            rolActual = (usuario.rolname).upper()
            if rolActual == 'ARTISTA':
                return render(request, 'gestor_artes/menu_operador.html', {'mensaje': f'Bienvenido {usuario.username}'})
            if rolActual == 'ADMIN':
                return render(request, 'gestor_artes/menu_admin.html', {'mensaje': f'Bienvenido {usuario.username}'})
            return render(request, 'gestor_artes/login.html', {'mensaje': 'Rol no reconocido'})

        return render(request, 'gestor_artes/login.html', {'r2': 'Error De Usuario o Contraseña!!'})

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
    mensaje = ''
    return render(request, 'gestor_artes/login.html', {'mensaje': mensaje})

def cerrarSesion(request):
    try:
        del request.session['usuario']
    except Exception:
        pass
    return render(request, 'gestor_artes/login.html', {'mensaje': 'Sesión cerrada'})

def mostrarMenuAdmin(request):
    auth_check = verificar_sesion(request)
    if auth_check:
        return auth_check
    return render(request, 'gestor_artes/menu_admin.html')

def mostrarMenuOperador(request):
    auth_check = verificar_sesion(request)
    if auth_check:
        return auth_check
    return render(request, 'gestor_artes/menu_operador.html')

def mostrarListarColaboraciones(request):
    auth_check = verificar_sesion(request)
    if auth_check:
        return auth_check
    colaboraciones = Colaboraciones.objects.all()
    datos = {'colaboraciones': colaboraciones}
    return render(request, 'gestor_artes/listar_colaboraciones.html', datos)

def mostrarFormRegistrarColaboracion(request):
    auth_check = verificar_sesion(request)
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
    auth_check = verificar_sesion(request)
    if auth_check:
        return auth_check
    return render(request, 'gestor_artes/listar_historial.html', {
        'historial': [],
    })

def mostrarFormCrearProyecto(request):
    auth_check = verificar_sesion(request)
    if auth_check:
        return auth_check
    return render(request, 'gestor_artes/form_crear_proyecto.html')

def registrarProyecto(request):
    auth_check = verificar_sesion(request)
    if auth_check:
        return auth_check
    if request.method != 'POST':
        return render(request, 'gestor_artes/form_crear_proyecto.html', {'mensaje': 'Método no permitido'})

    titulo = request.POST.get('titulo', '').strip()
    if not titulo:
        return render(request, 'gestor_artes/form_crear_proyecto.html', {'mensaje': 'El título es obligatorio'})

    p = Proyecto(titulo=titulo)
    p.save()
    return render(request, 'gestor_artes/menu_admin.html', {'mensaje': f'Proyecto "{titulo}" creado'})

# Funciones de filtrado (de la versión local)
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