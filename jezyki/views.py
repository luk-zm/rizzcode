from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Language

def jezyki(request):
    languages = Language.objects.all().values()
    template = loader.get_template('proglan.html')
    context = {
        'languages': languages,
    }
    return HttpResponse(template.render(context, request))
