from django.urls import path
from .views import *

urlpatterns = [
    path('inicio/', cargar_inicio),
    path('libros/', cargar_vista_libros),
    path('datos_covid/',get_datos_covid),
    path('libros/crear/', crear_libro, name='crear_libro'),
    path('libros/<int:id>',detalle_libro, name='detalle_libro'),
    path('libros/editar/<int:id>', editar_libro, name='editar_libro'),
    path('libros/borrar/<int:id>', borrar_libro, name='borrar_libro')
]