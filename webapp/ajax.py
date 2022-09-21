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
        
        if request.is_ajax() and request.POST.get('type') == 'change_status':
            id = request.POST.get('id')
            profesor = Profesor.objects.get(id=id)
            if profesor.activo:
                profesor.activo = False
            else:
                profesor.activo = True
            profesor.save()
            return JsonResponse({'message': 'Profesor eliminado con exito'}, status=200)

        if request.is_ajax() and request.POST.get('type') == 'data_profesor':
            print('entro'+'-'*50)
            # obtener el id del profesor
            id = request.POST.get('id')
            # obtener el objeto
            profesor = Profesor.objects.get(id=id)
            data = {
                'id': profesor.id,
                'nombre': profesor.nombre,
                'alias': profesor.alias,
                'activo': profesor.activo,
            }
            return JsonResponse(data, status=200)

        if request.is_ajax() and request.POST.get('type') == 'update_profesor':
            # obtener el id del profesor
            id = request.POST.get('id')
            profesor = ProfesorForm(
                request.POST, instance=Profesor.objects.get(id=id))
            if profesor.is_valid():
                profesor.save()
                return JsonResponse({'message': 'Profesor actualizado con exito'}, status=200)
            html_form = str(profesor)
            return JsonResponse({'form': html_form}, status=400)

        if request.is_ajax() and request.POST.get('type') == 'delete':
            id = request.POST.get('id')
            profesor = Profesor.objects.get(id=id)
            profesor.delete()
            return JsonResponse({'message': 'Profesor eliminado con exito'}, status=200)

        
        if request.is_ajax() and request.POST.get('type') == 'form_update_data_profesor':
            id = request.POST.get('id')
            profesor = Profesor.objects.get(id=id)
            form = ProfesorForm(instance=profesor)
            html_form = str(form)
            return JsonResponse({'form': html_form}, status=200)

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
        if 'consulta' in request.POST:
            consulta = request.POST['consulta']
            materias = list(Materia.objects.filter(grado=consulta).values())
            return JsonResponse(materias, safe=False)
        materias = list(Materia.objects.all().values())
        for materia in materias:
            materia['grado'] = Grado.objects.get(id=materia['grado_id']).nombre
        return JsonResponse(materias, safe=False)

# Horario


class HorariosAjax(ListView):
    model = Horario

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        # lista de horarios solo los activos
        horarios = list(Horario.objects.filter(activo=True).values())

        return JsonResponse(horarios, safe=False)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        horarios = list(Horario.objects.filter(activo=True).values())
        return JsonResponse(horarios, safe=False)

# Asignatura


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

# Periodo


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
