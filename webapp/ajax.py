from xml.dom import ValidationErr
from django.http import JsonResponse
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.core.exceptions import ValidationError

from .models import *
from .forms import *

from .functionHorario import *


class ProfesoresAjax(ListView):
    model = Profesor
    form_class = ProfesorForm

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        profesores = list(Profesor.objects.all().values())
        return JsonResponse(profesores, safe=False)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        try:
            print('-'*64)
            id = request.POST.get('id', None)
            type_request = request.POST.get('type', None)
            if request.is_ajax():
                if type_request == 'data_profesor':
                    profesor = Profesor.objects.get(id=id)
                    data = {
                        'id': profesor.id,
                        'nombre': profesor.nombre,
                        'alias': profesor.alias,
                        'activo': profesor.activo,
                    }
                    return JsonResponse(data, status=200)

                if type_request == 'add_profesor':
                    form = self.form_class(request.POST)
                    if form.is_valid():
                        form.save()
                        return JsonResponse({'message': 'Profesor agregado con exito'}, status=200)
                    html_form = str(form)
                    return JsonResponse({'form': html_form}, status=400)

                if type_request == 'update_profesor':
                    profesor = ProfesorForm(
                        request.POST, instance=Profesor.objects.get(id=id))
                    if profesor.is_valid():
                        profesor.save()
                        return JsonResponse({'message': 'Profesor actualizado con exito'}, status=200)
                    html_form = str(profesor)
                    return JsonResponse({'form': html_form, 'nombre': profesor.nombre}, status=400)

                if type_request == 'form_update_data_profesor':
                    profesor = Profesor.objects.get(id=id)
                    form = ProfesorForm(instance=profesor)
                    html_form = str(form)
                    return JsonResponse({'form': html_form, 'nombre': profesor.nombre}, status=200)

                if type_request == 'change_status':
                    profesor = Profesor.objects.get(id=id)
                    if profesor.activo:
                        profesor.activo = False
                    else:
                        profesor.activo = True
                    profesor.save()
                    return JsonResponse({'message': 'Profesor eliminado con exito'}, status=200)

                if type_request == 'delete':
                    profesor = Profesor.objects.get(id=id)
                    # cambiar el estado del modelo
                    profesor.status_model = False
                    profesor.save()
                    return JsonResponse({'message': 'Profesor eliminado con exito'}, status=200)
            # filtrar por  'status_model' = True
            profesores = list(Profesor.objects.filter(
                status_model=True).values())
            return JsonResponse(profesores, safe=False)
        except Exception as e:
            print(e)
            return JsonResponse({'message': str(e)}, status=400)


class GradosAjax(ListView):
    model = Grado
    form_class = GradoForm

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        grados = list(Grado.objects.all().values())
        return JsonResponse(grados, safe=False)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        try:
            id = request.POST.get('id', None)
            type_request = request.POST.get('type', None)
            if request.is_ajax():
                if type_request == 'data_grado':
                    grado = Grado.objects.get(id=id)
                    data = {
                        'nombre': grado.nombre,
                        'alias': grado.alias,
                        'activo': grado.activo,
                    }
                    return JsonResponse(data, status=200)

                if type_request == 'add_grado':
                    form = self.form_class(request.POST)
                    if form.is_valid():
                        form.save()
                        return JsonResponse({'message': 'Grado agregado con exito'}, status=200)
                    html_form = str(form)
                    return JsonResponse({'form': html_form}, status=400)

                if type_request == 'update_grado':
                    grado = GradoForm(
                        request.POST, instance=Grado.objects.get(id=id))
                    if grado.is_valid():
                        grado.save()
                        return JsonResponse({'message': 'Grado actualizado con exito'}, status=200)
                    html_form = str(grado)
                    return JsonResponse({'form': html_form, 'nombre': grado.nombre}, status=400)

                if type_request == 'form_update_data_grado':
                    grado = Grado.objects.get(id=id)
                    form = GradoForm(instance=grado)
                    html_form = str(form)
                    return JsonResponse({'form': html_form, 'nombre': grado.nombre}, status=200)

                if type_request == 'change_status':
                    grado = Grado.objects.get(id=id)
                    if grado.activo:
                        grado.activo = False
                    else:
                        grado.activo = True
                    grado.save()
                    return JsonResponse({'message': 'Grado eliminado con exito'}, status=200)

                if type_request == 'delete':
                    materias = Materia.objects.filter(grado=id)
                    for materia in materias:
                        materia.status_model = False
                        materia.save()
                    grado = Grado.objects.get(id=id)
                    # cambiar el estado del modelo
                    grado.status_model = False
                    grado.save()
                    return JsonResponse({'message': 'Grado eliminado con exito'}, status=200)
            grados = list(Grado.objects.filter(status_model=True).values())
            return JsonResponse(grados, safe=False)
        except Exception as e:
            print(e)
            return JsonResponse({'message': str(e)}, status=400)


class MateriasAjax(ListView):
    model = Materia

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        materias = list(Materia.objects.all().values())
        return JsonResponse(materias, safe=False)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        try:
            id = request.POST.get('id', None)
            type_request = request.POST.get('type', None)
            if request.is_ajax():
                if type_request == 'add_materia':
                    form = MateriaForm(request.POST)
                    if form.is_valid():
                        form.save()
                        return JsonResponse({'message': 'Materia agregada con exito'}, status=200)
                    html_form = str(form)
                    return JsonResponse({'form': html_form}, status=400)

                if type_request == 'update_materia':
                    materia = MateriaForm(
                        request.POST, instance=Materia.objects.get(id=id))
                    if materia.is_valid():
                        materia.save()
                        return JsonResponse({'message': 'Materia actualizada con exito'}, status=200)
                    html_form = str(materia)
                    return JsonResponse({'form': html_form, 'nombre': materia.nombre}, status=400)

                if type_request == 'form_update_data_materia':
                    materia = Materia.objects.get(id=id)
                    form = MateriaForm(instance=materia)
                    html_form = str(form)
                    return JsonResponse({'form': html_form, 'nombre': materia.nombre}, status=200)

                if type_request == 'form_add_data_materia':
                    form = MateriaForm()
                    # agregar el valor inicial de grado de acuerdo con el id del request id_grado
                    id_grado = request.POST.get('id_grado', None)
                    form.fields['grado'].initial = id_grado
                    html_form = str(form)
                    return JsonResponse({'form': html_form}, status=200)

                if type_request == 'change_status':
                    materia = Materia.objects.get(id=id)
                    if materia.activo:
                        materia.activo = False
                    else:
                        materia.activo = True
                    materia.save()
                    return JsonResponse({'message': 'Materia eliminada con exito'}, status=200)

                if type_request == 'delete':
                    materia = Materia.objects.get(id=id)
                    # cambiar el estado del modelo
                    materia.status_model = False
                    materia.save()
                    return JsonResponse({'message': 'Materia eliminada con exito'}, status=200)

            materias = list(Materia.objects.filter(status_model=True).values())
            for materia in materias:
                materia['grado'] = Grado.objects.get(
                    id=materia['grado_id']).nombre
            return JsonResponse(materias, safe=False)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=400)


class NewHorarioAjax(ListView):
    model = Horario
    form = NewHorarioForm

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            form = self.form(request.POST)
            if form.is_valid():
                form.save()
                return JsonResponse({'message': 'Horario agregado con exito', 'id': form.instance.id}, status=200)
            html_form = str(form)
            return JsonResponse({'form_html': html_form}, status=400)

import sys
class PlantillaAjax(ListView, GeneradorHorario):

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        try:
            type = request.POST.get('type')
            id_horario = request.POST.get('id_horario')
            if request.is_ajax():
                if type == 'check_dias':
                    dia = request.POST.get('dia', None)
                    self.change_checkbox(dia, id_horario)
                    return JsonResponse({'message': 'Dias actualizados con exito'}, status=200)
                if type == 'agregar_receso':
                    pass

                horarioModel = Horario.objects.get(id=id_horario)
                if type == 'hora_inicio':
                    hora_previa = horarioModel.hora_inicio
                    hora_inicio = request.POST.get('hora', None)
                    horarioModel.hora_inicio = hora_inicio
                    horarioModel.save()
                    return JsonResponse({'message': 'Hora de inicio actualizada con exito'}, status=200)
                if type == 'no_periodos':
                    horarioModel.cantidad_periodo = request.POST.get('no_periodos')
                    horarioModel.save()
                    return JsonResponse({'message': 'Numero de periodos actualizado con exito'}, status=200)
                if type == 'duracion_periodo':
                    horarioModel.duracion_periodo_hour = request.POST.get('hora')
                    horarioModel.duracion_periodo_minute = request.POST.get('minuto')
                    horarioModel.save()
                    return JsonResponse({'message': 'Duracion de periodos actualizada con exito'}, status=200)
                horario = self.nw_horario_generador(dias_activos=horarioModel.Dias_list(), 
                    hora_inicio=horarioModel.hora_inicio.strftime('%H:%M'), intervalo=horarioModel.Duracion_str(), no_periodos=horarioModel.cantidad_periodo)
                if type == 'dias_activos':
                    return JsonResponse(horarioModel.Dias_dict(), safe=False, status=200)
                if type == 'generador':
                    horario = self.horario_JSON(horario)
                    return JsonResponse(horario, status=200, safe=False)
                else:
                    return JsonResponse({'message': 'error'}, status=400)
        except ValidationError as e:
            if type == 'hora_inicio':
                return JsonResponse({
                    'message': 'La hora de inicio debe tener un formato 00:00',
                    'hora': str(hora_previa)[:5],
                    }, status=400)
            return JsonResponse({'message': str(e)}, status=400)
        except Exception as e:
            print('Error: ', sys.exc_info()[0])
            return JsonResponse({'message': str(e)}, status=400)


class HorariosAjax(ListView, GeneradorHorario):
    model = Horario

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        # lista de horarios solo los activos
        horarios = list(Horario.objects.filter(activo=True).values())

        return JsonResponse(horarios, safe=False)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            try:
                type_request = request.POST.get('type', None)
                if type_request == 'nw_plantilla':
                    return JsonResponse(self.nw_plantilla(), safe=False)
                horarios = list(Horario.objects.filter(
                    status_model=True).values())
                return JsonResponse(horarios, safe=False)
            except Exception as e:
                return JsonResponse({'message': str(e)}, status=400)


class SelectProfesorAjax(ListView):
    model = Profesor

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        try:
            id = request.GET.get('id', None)
            profesores = list(Profesor.objects.filter(
                materia=id, activo=True).values())
            return JsonResponse(profesores, safe=False)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=400)


class SelectGradoAjax(ListView):
    model = Grado

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        try:
            id = request.GET.get('id', None)
            grados = list(Grado.objects.filter(
                materia=id, activo=True).values())
            return JsonResponse(grados, safe=False)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=400)


class SelectMateriaAjax(ListView):
    model = Materia

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        try:
            id = request.GET.get('id', None)
            materias = list(Materia.objects.filter(
                grado=id, activo=True).values())
            return JsonResponse(materias, safe=False)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=400)


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
