from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.

def zadania(request):
    return HttpResponse("Exercise page")
