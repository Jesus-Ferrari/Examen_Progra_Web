from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('quienes_somos/', views.quienes_somos, name="quienes_somos"),
    path('categorias/', views.categorias, name="categorias"),
    path('autores/', views.autores, name="autores"),
    path('libros/', views.libros, name="libros"),
]