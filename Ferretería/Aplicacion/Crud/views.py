from django.shortcuts import render, redirect
from .models import Crud
from .models import SistemaViajes
from .models import Manager
from django.shortcuts import render

# Create your views here.


def home(request):
    cursos = Crud.objects.all()
    return render(request, "index.html", {"cursos": cursos})


def administrador(request):
    viajes = SistemaViajes.objects.all()
    return render(request, "Administrador.html", {"viajes": viajes})


def verNuevosProductos(request):
    cursos = Crud.objects.all()
    return render(request, "verNuevosProductos.html", {"cursos": cursos})


def AnadirProductos(request):
    cursos = Crud.objects.all()
    return render(request, "AnadirProductos.html", {"cursos": cursos})


def registrarCurso(request):
    code = request.POST["txtCodigo"]
    name = request.POST["txtNombre"]
    credits = request.POST["numCreditos"]

    cursos = Crud.objects.create(codigo=code, nombre=name, creditos=credits)
    return redirect("/AnadirProductos")


def edicionCurso(request, codigo):
    curso = Crud.objects.get(codigo=codigo)
    return render(request, "edicionCurso.html", {"curso": curso})


def editarCurso(request):
    codigo = request.POST["txtCodigo"]
    nombre = request.POST["txtNombre"]
    creditos = request.POST["numCreditos"]

    curso = Crud.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()

    return redirect("/AnadirProductos")


def eliminarCurso(request, codigo):
    curso = Crud.objects.get(codigo=codigo)
    curso.delete()

    return redirect("/AnadirProductos")


# ---------------------------------------------------------------------------#
def registrarViaje(request):
    num_viaje = request.POST["txtViaje"]
    articulos = request.POST["txtArticulos"]
    hora_entrega_estimado = request.POST["hora_entrega_estimado"]
    turno = request.POST["num_Turno"]
    direccion = request.POST["txtDireccion"]
    num_telefono = request.POST["num_telefono"]

    viajes = SistemaViajes.objects.create(
        num_viaje=num_viaje,
        articulos=articulos,
        hora_entrega_estimado=hora_entrega_estimado,
        turno=turno,
        direccion=direccion,
        num_telefono=num_telefono,
    )
    return redirect("/Administrador/")


def verNuevosViajes(request):
    viajes = SistemaViajes.objects.all()
    return render(request, "Administrador.html", {"viajes": viajes})


def repartoViajes(request):
    viajes = SistemaViajes.objects.all()
    return render(request, "repartoViajes.html", {"viajes": viajes})


def edicionViaje(request, num_viaje):
    viaje = SistemaViajes.objects.get(num_viaje=num_viaje)
    return render(request, "edicionViaje.html", {"viaje": viaje})


def editarViaje(request):
    num_viaje = request.POST["txtViaje"]
    articulos = request.POST["txtArticulos"]
    hora_entrega_estimado = request.POST["hora_entrega_estimado"]
    turno = request.POST["num_Turno"]
    direccion = request.POST["txtDireccion"]
    num_telefono = request.POST["num_telefono"]

    viaje = SistemaViajes.objects.get(num_viaje=num_viaje)
    viaje.articulos = articulos
    viaje.hora_entrega_estimado = hora_entrega_estimado
    viaje.turno = turno
    viaje.direccion = direccion
    viaje.num_telefono = num_telefono

    viaje.save()

    return redirect("/Administrador/")


def eliminarViaje(request, num_viaje):
    viaje = SistemaViajes.objects.get(num_viaje=num_viaje)
    viaje.delete()

    return redirect("/Administrador/")


# -----------------------------------------------------------------------
def conocenos(request):
    manager = Manager.objects.all()
    return render(request, "Conocenos.html", {"manager": manager})


def correoManager(request):
    manager = Manager.objects.all()
    return render(request, "correoManager.html", {"manager": manager})


def RegistrarManager(request):
    codigo_manager = request.POST["txtcodigo_manager"]
    correo = request.POST["txtcorreo"]

    manager = Manager.objects.create(codigo_manager=codigo_manager, correo=correo)
    return redirect("/CorreoManager")


def edicionManager(request, codigo_manager):
    manager = Manager.objects.get(codigo_manager=codigo_manager)
    return render(request, "correoManager.html", {"manager": manager})


def editarManager(request):
    codigo_manager = request.POST["txtcodigo_manager"]
    correo = request.POST["txtcorreo"]

    manager = Manager.objects.get(codigo_manager=codigo_manager)
    manager.correo = correo

    manager.save()

    return redirect("/CorreoManager")


def eliminarManager(request, codigo_manager):
    manager = Manager.objects.get(codigo_manager=codigo_manager)
    manager.delete()

    return redirect("/CorreoManager")
