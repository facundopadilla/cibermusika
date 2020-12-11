from django.contrib import admin
from .models import Contacto, Telefono
# Register your models here.

class TelefonoAdmin(admin.StackedInline):
    model = Telefono

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    inlines = [TelefonoAdmin]

    class Meta:
        model = Contacto
