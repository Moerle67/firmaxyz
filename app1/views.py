from django.shortcuts import render
from .models import *

# Create your views here.

def hello(request):
    name = "Hans Hustensaft Apfelbaum"
    context = {
        'name' : name
    }
    return render(request, 'app1/hello2.html', context)

def seite2(request):
    name = "Hans Hustensaft Apfelbaum"
    text = "oder ein ganz anderer"
    ds = Text.objects.get(key="text1")
    text1 = ds.text
    context = {
        'name' : name,
        'farbe' : 'warning',
        'text' : text,
        'text1' : text1
    }
    return render(request, 'app1/hello3.html', context)