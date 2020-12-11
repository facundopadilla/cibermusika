from django.db import models

# Create your models here.
class Contacto(models.Model):
    direccion = models.CharField(max_length=400, verbose_name="Dirección")
    horario = models.CharField(max_length=150, verbose_name="Horarios")
    tel = models.CharField(max_length=50, verbose_name="Teléfono")

    def __str__(self):
        return "Contacto"

class Telefono(models.Model):
    tel = models.ForeignKey(Contacto, on_delete=models.CASCADE, default=None, verbose_name="Teléfono")
    phone = models.CharField(max_length=50, verbose_name="Teléfono", null=True, blank=True)

    def __str__(self):
        return self.phone
    
    class Meta:
        verbose_name = "Teléfono"
        verbose_name_plural = "Teléfonos"

    