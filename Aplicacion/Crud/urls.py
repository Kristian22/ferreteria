from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    # -----------------------------------------------
    path("verNuevosProductos/", views.verNuevosProductos),
    path("gestionCrud/", views.home),
    path("registrarCurso/", views.registrarCurso),
    path("Administrador/", views.administrador),
    path("AnadirProductos/", views.AnadirProductos),
    path("AnadirProductos/edicionCurso/<codigo>", views.edicionCurso),
    path("editarCurso/", views.editarCurso),
    path("AnadirProductos/eliminarCurso/<codigo>", views.eliminarCurso),
    # -----------------------------------------------
    path("Administrador/registrarViaje/", views.registrarViaje),
    path("verNuevosViajes/", views.verNuevosViajes),
    path("repartoViajes/", views.repartoViajes),
    path("editarViaje/", views.editarViaje),
    path("Administrador/edicionViaje/<num_viaje>", views.edicionViaje),
    path("Administrador/eliminarViaje/<num_viaje>", views.eliminarViaje),
    path("Conocenos/", views.conocenos),
    # ----------------------------------------------
    path("CorreoManager/", views.correoManager),
    path("RegistrarManager/", views.RegistrarManager),
    path("CorreoManager/edicionManager/<codigo_manager>", views.edicionManager),
    path("CorreoManager/eliminarManager/<codigo_manager>", views.eliminarManager),
    path("editarManager/", views.editarManager),
]
