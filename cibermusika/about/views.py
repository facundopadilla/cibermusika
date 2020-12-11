from django.views.generic import TemplateView
from .models import Equipo
# Create your views here.

class AboutView(TemplateView):
    template_name = "about/about.html"

    def get_context_data(self, *args, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['equipo'] = Equipo.objects.all()
        return context