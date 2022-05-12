from django.urls import path
from .views import *

urlpatterns = [
    path('libros/', obtener_libros_json),
    #path('libros/crear/', crear_libro, name='crear_libro'),
    #path('libros/<int:id>',detalle_libro, name='detalle_libro'),
]