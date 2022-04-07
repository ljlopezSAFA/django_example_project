from django.shortcuts import render,redirect
from .models import *


# Create your views here.

def cargar_inicio(request):
    return render(request, 'inicio.html')


def cargar_vista_libros(requests):
    lista_libros = Libro.objects.all()
    return render(requests,'libros.html', {'libros': lista_libros})


def crear_libro(request):
    # Método para operación CRUD Crear nuevo libro
    if request.method == 'POST':
        # En caso de que no exista id quiere decir que no existe y hay que crearlo
        libro = Libro()
        libro.id = request.POST.get('id')
        libro.nombre = request.POST.get('nombre')
        libro.num_paginas = request.POST.get('num_paginas')
        libro.fecha_publicacion = request.POST.get('fecha')
        libro.editorial = Editorial.objects.get(id=1)
        Libro.save(libro)
        return redirect('/libreria/libros')
    else:
        return render(request, 'crear_libro.html')


def detalle_libro(request, id):
    libro = Libro.objects.get(id=id)
    context = {'libro': libro}
    return render(request, 'libro_detalle.html', context)




