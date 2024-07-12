from django.db import models

# Create your models here.
    
class Autor(models.Model):
    nombre              = models.CharField(max_length=30)
    nacionalidad        = models.CharField(max_length=20)

    def __str__(self):
        return str(self.nombre)
    
class Categoria(models.Model):
    nombre_categoria        = models.CharField(max_length=20)
    descripcion_categoria   = models.TextField(max_length=500)

    def __str__(self):
        return str(self.nombre_categoria)

class Libro(models.Model):
    titulo_libro        = models.CharField(max_length=100)
    anio_publicacion    = models.IntegerField()
    descripcion_breve   = models.TextField(max_length=500)
    categoria           = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    autor               = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.titulo_libro)

    
class NavItem(models.Model):
    titulo_nav_item         = models.CharField(max_length=40)
    url_nav_item            = models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.titulo_nav_item)
