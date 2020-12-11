from .models import RedSocial

def ctx_dict(request):
    redes = RedSocial.objects.all().first()

    return {'facebook':redes.facebook,
             'twitter':redes.twitter,
             'instagram':redes.instagram,
             'youtube':redes.youtube,
             'whatsapp':redes.whatsapp}