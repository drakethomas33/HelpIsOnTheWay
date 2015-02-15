from django.conf import settings

def ga_key(request):
    return {'ga_key': settings.GOOGLE_ANALYTICS_KEY}
