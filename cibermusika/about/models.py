from django.db import models

# Create your models here.

class Equipo(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombres")
    profesion = models.CharField(max_length=150, verbose_name="Profesión")
    imagen = models.ImageField(verbose_name="Foto")
    facebook = models.CharField(max_length=400, verbose_name="Facebook", null=True, blank=True)
    instagram = models.CharField(max_length=400, verbose_name="Instagram", null=True, blank=True)
    twitter = models.CharField(max_length=400, verbose_name="Twitter", null=True, blank=True)
    whatsapp = models.CharField(max_length=400, verbose_name="Whatsapp", null=True, blank=True)
    youtube = models.CharField(max_length=400, verbose_name="Youtube", null=True, blank=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"