from django.views.generic import TemplateView
from .models import Contacto, Telefono
# Create your views here.

class ContactView(TemplateView):
    template_name = "contact/contact.html"

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['contacto'] = Contacto.objects.all().first()
        context['telefonos'] = Telefono.objects.all()
        return context