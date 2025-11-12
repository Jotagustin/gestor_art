from django.shortcuts import render
from .models import Colaboraciones, Proyecto, Artistas

# 🧩 Login / Sesión
def mostrarLogin(request):
    pass

def iniciarSesion(request):
    pass

def cerrarSesion(request):
    pass


# 🧩 Menús
def mostrarMenuAdmin(request):
    pass

def mostrarMenuOperador(request):
    pass


# 🧩 Colaboraciones (Operador)
def mostrarListarColaboraciones(request):
    colaboraciones = Colaboraciones.objects.all()
    datos = {'colaboraciones': colaboraciones}
    return render(request, 'gestor_artes/listar_colaboraciones.html', datos)


def mostrarFormRegistrarColaboracion(request):
    pass

def registrarColaboracion(request):
    pass

def mostrarFormActualizarColaboracion(request):
    pass

def actualizarColaboracion(request):
    pass

def eliminarColaboracion(request):
    pass


# 🧩 Historial (Admin)
def mostrarListarHistorial(request):
    pass


def filtroEmpieza(request):
    filtro = request.POST['txtfil']
    colabs = Colaboraciones.objects.filter(proyecto__titulo__istartswith=filtro)
    datos = {'colaboraciones': colabs}
    return render(request, 'gestor_artes/listar_colaboraciones.html', datos)

def filtroContenga(request):
    filtro = request.POST['txtfil']
    colabs = Colaboraciones.objects.filter(artista__nombre__icontains=filtro)
    datos = {'colaboraciones': colabs}
    return render(request, 'gestor_artes/listar_colaboraciones.html', datos)

def filtroEntre(request):
    val1 = request.POST['txtval1']
    val2 = request.POST['txtval2']
    colabs = Colaboraciones.objects.filter(valor__range=(val1, val2))
    datos = {'colaboraciones': colabs}
    return render(request, 'gestor_artes/listar_colaboraciones.html', datos)