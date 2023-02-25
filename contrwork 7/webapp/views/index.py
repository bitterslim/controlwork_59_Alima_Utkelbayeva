from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from webapp.models import Guest


def index_view(request: WSGIRequest):
    guest = Guest.objects.exclude(status="blocked")
    context = {
        'guest': guest
    }
    return render(request, 'index.html', context=context)
