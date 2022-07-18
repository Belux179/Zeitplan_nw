from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'web/home.html')


def aula(request):
    return render(request, 'web/aula.html')


def grado(request):
    return render(request, 'web/grado.html')


def profesor(request):
    return render(request, 'web/profesor.html')
