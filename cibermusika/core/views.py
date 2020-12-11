from django.views.generic import TemplateView
from .models import RedSocial, NoticiaPrincipal, Categoria, Noticias
# Create your views here.

class IndexView(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['redsocial'] = RedSocial.objects.all().first()
        context['noticiap'] =  NoticiaPrincipal.objects.all().first()
        context['noticias'] = Noticias.objects.all()
        context['categorias'] = Categoria.objects.all()
        return context
    