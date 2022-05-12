from django.shortcuts import render,redirect
from .models import *
from django.http import JsonResponse
import requests

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


def get_datos_covid(request):
    datos_covid = requests.get("https://api.covidtracking.com/v1/us/current.json").json()
    positivos = datos_covid[0]["positive"]
    hospitalizaciones = datos_covid[0]["hospitalizedCurrently"]
    muertes = datos_covid[0]["death"]
    return render(request, 'covid_detalle.html', {'positivos': positivos , 'hospitalizaciones': hospitalizaciones, 'muertes': muertes})





def obtener_libros_json(requests):
    libros = Libro.objects.all()
    return JsonResponse(list(libros.values()), safe=False)




