from .models import Categoria

def ctx_dict(request):
    return {"categorias": Categoria.objects.all()}