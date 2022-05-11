from django.shortcuts import render,redirect
from .models import *
from .forms import *


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

def crear_libro_form(request):
    # Método para operación CRUD Crear nuevo libro
    if request.method == 'POST':
        return redirect('/libreria/libros')
    else:
        form_libro = Formulario_libro()
        return render(request, 'crear_libro_form.html', {'formulario_libro': form_libro})


def editar_libro(request,id):
    if request.method == "GET":
        libro = Libro.objects.get(id=id)
        return render(request, 'editar_libro.html', {'libro': libro})
    else:
        libro = Libro()
        libro.id = id
        libro.nombre = request.POST.get('nombre')
        libro.num_paginas = request.POST.get('num_paginas')
        libro.fecha_publicacion = request.POST.get('fecha')
        libro.editorial = Editorial.objects.get(id=1)
        Libro.save(libro)
        return redirect('/libreria/libros')



def detalle_libro(request, id):
    libro = Libro.objects.get(id=id)
    context = {'libro': libro}
    return render(request, 'libro_detalle.html', context)


def borrar_libro(request,id):
    libro = Libro.objects.get(id=id)
    if libro is not None:
        Libro.delete(libro)
    return redirect('/libreria/libros')




