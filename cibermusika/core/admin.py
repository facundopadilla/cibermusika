from django.contrib import admin
from .models import RedSocial, NoticiaPrincipal, Categoria, Noticias

# Register your models here.

class NoticiaPrincipalAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class NoticiasAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(RedSocial)
admin.site.register(NoticiaPrincipal, NoticiaPrincipalAdmin)
admin.site.register(Categoria)
admin.site.register(Noticias, NoticiasAdmin)