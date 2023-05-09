from django.shortcuts import render

# Create your views here.

def hello(request):
    name = "Hans Hustensaft Apfelbaum"
    context = {
        'name' : name
    }
    return render(request, 'app1/hello.html', context)
