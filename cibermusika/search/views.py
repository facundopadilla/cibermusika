from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, TemplateView
from .models import Musica, Categoria
from django.db.models import Q
# Create your views here.

class SearchView(ListView):
    template_name = 'search/search.html'
    paginate_by = 3
    model = Musica
    context_object_name = 'todo'

    def dispatch(self, request, *args, **kwargs):
        if request.GET.get('cancion'):
            return redirect(reverse('filterview', kwargs={"cancion": request.GET.get('cancion')}))
        return super(SearchView, self).dispatch(request, *args, **kwargs)

class FilterView(TemplateView):
    template_name = 'search/search.html'
    model = Musica

    def get_context_data(self, **kwargs):
        context = super(FilterView, self).get_context_data(**kwargs)
        context['canciones'] = Musica.objects.filter(Q(titulo__icontains = self.kwargs['cancion']))
        return context

