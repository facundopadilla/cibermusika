from django.views.generic import TemplateView
# Create your views here.

class CoursesView(TemplateView):
    template_name = "courses/courses.html"

    