from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class RedSocial(models.Model):
    facebook = models.CharField(max_length=400, null=True, blank=True)
    twitter = models.CharField(max_length=400, null=True, blank=True)
    youtube = models.CharField(max_length=400, null=True, blank=True)
    instagram = models.CharField(max_length=400, null=True, blank=True)
    whatsapp = models.CharField(max_length=400, null=True, blank=True)

    def __str__(self):
        return "Redes sociales"
    
    class Meta:
        verbose_name = "Redes sociales"
        verbose_name_plural = "Redes sociales"

class NoticiaPrincipal(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    link_youtube = models.CharField(max_length=400, verbose_name="ID de Youtube")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    def __str__(self):
        return "Noticia: " + self.titulo

    class Meta:
        ordering = ['-created']
        verbose_name = "Noticia principal"
        verbose_name_plural = "Noticia principal"

class Categoria(models.Model):
    categoria = models.CharField(max_length=100, verbose_name="Categoría")
    
    def __str__(self):
        return self.categoria

class Noticias(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Seleccionar categoría")
    descripcion = models.TextField(verbose_name="Descripción")
    audio = models.TextField(verbose_name="Link del MP3")
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    imagen = models.ImageField(verbose_name="Imagen", null=True, blank=True)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['-created']
        verbose_name = "Noticias"
        verbose_name_plural = "Noticias"
