from django.shortcuts import render
from .models import Categoria, Autor, Libro, NavItem

def index(request):
    NavItems = NavItem.objects.all()
    return render (request, 'projectLibrary/index.html', {"NavItems":NavItems})

def categorias(request):
    NavItems = NavItem.objects.all()
    categorias = Categoria.objects.all()
    return render (request, 'projectLibrary/categorias.html', {"NavItems":NavItems, "categorias":categorias})

def autores(request):
    NavItems = NavItem.objects.all()
    autores = Autor.objects.all()
    return render (request, 'projectLibrary/autores.html', {"NavItems":NavItems,"autores":autores})

def libros(request):
    NavItems = NavItem.objects.all()
    libros = Libro.objects.all()
    return render (request, 'projectLibrary/libros.html', {"NavItems":NavItems,"libros":libros})

def quienes_somos(request):
    NavItems = NavItem.objects.all()
    return render (request, 'projectLibrary/quienes_somos.html', {"NavItems":NavItems})


