from django.views.generic import TemplateView
# Create your views here.

class AboutView(TemplateView):
    template_name = "about/about.html"