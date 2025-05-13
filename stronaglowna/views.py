from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Strona główna. Zastąpić klasą i templatem.")


# Create your views here.
