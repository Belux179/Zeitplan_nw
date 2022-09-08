from django.http import JsonResponse
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *

class ProfesoresAjax(ListView):
    model = Profesor

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        profesores = list(Profesor.objects.all().values())
        return JsonResponse(profesores, safe=False)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        profesores = list(Profesor.objects.all().values())
        return JsonResponse(profesores, safe=False)


# grado
class GradosAjax(ListView):
    model = Grado

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        grados = list(Grado.objects.all().values())
        return JsonResponse(grados, safe=False)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        grados = list(Grado.objects.all().values())
        return JsonResponse(grados, safe=False)

# materia
class MateriasAjax(ListView):
    model = Materia

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        materias = list(Materia.objects.all().values())
        return JsonResponse(materias, safe=False)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        materias = list(Materia.objects.all().values())
        return JsonResponse(materias, safe=False)

# Horario
class HorariosAjax(ListView):
    model = Horario

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        horarios = list(Horario.objects.all().values())
        return JsonResponse(horarios, safe=False)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        horarios = list(Horario.objects.all().values())
        return JsonResponse(horarios, safe=False)

#Asignatura
class AsignaturasAjax(ListView):
    model = Asignatura

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        asignaturas = list(Asignatura.objects.all().values())
        return JsonResponse(asignaturas, safe=False)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        asignaturas = list(Asignatura.objects.all().values())
        return JsonResponse(asignaturas, safe=False)

#Periodo
class PeriodosAjax(ListView):
    model = Periodo

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        periodos = list(Periodo.objects.all().values())
        return JsonResponse(periodos, safe=False)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        periodos = list(Periodo.objects.all().values())
        return JsonResponse(periodos, safe=False)