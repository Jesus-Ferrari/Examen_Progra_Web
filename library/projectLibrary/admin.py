from django.contrib import admin
from .models import Categoria, Autor, Libro, NavItem

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Autor)
admin.site.register(Libro)
admin.site.register(NavItem)

