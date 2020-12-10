from django.views.generic import TemplateView
# Create your views here.

class ContactView(TemplateView):
    template_name = "contact/contact.html"