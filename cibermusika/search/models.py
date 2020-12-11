from django.db import models

# Create your models here.


class Categoria(models.Model):
    category = models.CharField(max_length=101)

    def __str__(self):
        return self.category
    
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías / Géneros"

class Musica(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    descripcion = models.TextField(null=True, blank=True, verbose_name="Descripción")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Category")
    link = models.TextField(verbose_name="Link del MP3")
    imagen = models.ImageField(verbose_name="Imagen")

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = "Canción"
        verbose_name_plural = "Canciones"