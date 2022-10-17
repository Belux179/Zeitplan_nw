import sys
from django.http import JsonResponse
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.core.exceptions import ValidationError

from .models import *
from .forms import *

from .functionHorario import *


class UsuarioAjax(ListView):
    form = PreguntasForm

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        try:
            type = request.POST.get('type')
            usuario = request.user.id
            pregunta = request.POST.get('pregunta')
            respuesta = request.POST.get('respuesta')
            if type == 'frase':
                if pregunta != '' and respuesta != '':
                    try:
                        modelo = Pregunta.objects.get(usuario=usuario)
                        modelo.pregunta = pregunta
                        modelo.respuesta = respuesta
                        modelo.usuario = User.objects.get(id=usuario)
                        modelo.save()
                        return JsonResponse({'status': 'ok'})
                    except Exception as e:
                        return JsonResponse({'status': 'error'})
            return JsonResponse({'status': 'ok'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


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
                    nombre = profesor.nombre
                    profesor.nombre = str(nombre) + ' (Eliminado)'
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
                if type_request == 'form_html':
                    form = MateriaForm()
                    html_form = str(form)
                    return JsonResponse({'form': html_form}, status=200)

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
                    try:
                        receso = Recesos.objects.get(
                            periodo=request.POST.get('periodo'))
                    except Recesos.DoesNotExist:
                        receso = Recesos()
                    finally:
                        receso.periodo = request.POST.get('periodo')
                        receso.hora_duracion = request.POST.get('hora')
                        receso.minuto_duracion = request.POST.get('minuto')
                        receso.horario = Horario.objects.get(id=id_horario)
                        receso.save()
                        return JsonResponse({'message': 'Receso agregado con exito'}, status=200)
                if type == 'eliminar_receso':
                    receso = Recesos.objects.get(periodo=int(
                        request.POST.get('periodo'))-1, horario=id_horario)
                    receso.delete()
                    return JsonResponse({'message': 'Receso eliminado con exito'}, status=200)
                horarioModel = Horario.objects.get(id=id_horario)
                if type == 'hora_inicio':
                    hora_previa = horarioModel.hora_inicio
                    hora_inicio = request.POST.get('hora', None)
                    horarioModel.hora_inicio = hora_inicio
                    horarioModel.save()
                    return JsonResponse({'message': 'Hora de inicio actualizada con exito'}, status=200)
                if type == 'no_periodos':
                    horarioModel.cantidad_periodo = request.POST.get(
                        'no_periodos')
                    horarioModel.save()
                    return JsonResponse({'message': 'Numero de periodos actualizado con exito'}, status=200)
                if type == 'duracion_periodo':
                    horarioModel.duracion_periodo_hour = request.POST.get(
                        'hora')
                    horarioModel.duracion_periodo_minute = request.POST.get(
                        'minuto')
                    horarioModel.save()
                    return JsonResponse({'message': 'Duracion de periodos actualizada con exito'}, status=200)
                if type == 'dias_activos':
                    return JsonResponse(horarioModel.Dias_dict(), safe=False, status=200)
                recesos = self.recesos_dict(id_horario)
                horario = self.nw_horario_generador(dias_activos=horarioModel.Dias_list(),
                                                    recreos=recesos, hora_inicio=horarioModel.hora_inicio.strftime('%H:%M'), intervalo=horarioModel.Duracion_str(), no_periodos=horarioModel.cantidad_periodo)
                if type == 'generador':
                    horario = self.horario_JSON(horario)
                    return JsonResponse(horario, status=200, safe=False)

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

                if type_request == 'eliminar_horario':
                    # solo cambia el status_model
                    horario = Horario.objects.get(
                        id=request.POST.get('id_horario'))
                    horario.status_model = False
                    horario.save()
                    return JsonResponse({'message': 'Horario eliminado con exito'}, status=200)
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
    def post(self, request, *args, **kwargs):
        try:
            type = request.POST.get('type', None)
            if type == 'change_status':
                estadoprofesor = EstadoProfesorHorario.objects.get(
                    id=request.POST.get('id'))
                estadoprofesor.activo = not estadoprofesor.activo
                estadoprofesor.save()
                return JsonResponse({'message': 'Profesor actualizado con exito'}, status=200)
            id_horario = request.POST.get('id_horario')
            if type == 'condiciones':
                estado_profesor = EstadoProfesorHorario.objects.get(id=request.POST.get('id'))
                print(estado_profesor.cantidad_max_periodo)
                if estado_profesor.cantidad_max_periodo == 0:
                    estado_profesor.cantidad_max_periodo = Horario.objects.get(id=id_horario).Cantidad_periodos()
                    estado_profesor.save()
                form = EstadoProfesorHorarioForm(instance=estado_profesor)
                # separa el form en 2 partes
                print(dir(form))
                cantidad_max_periodo = str(form['cantidad_max_periodo'])
                Lunes = form['Lunes'].__str__()
                Martes = form['Martes'].__str__()
                Miercoles = form['Miercoles'].__str__()
                Jueves = form['Jueves'].__str__()
                Viernes = form['Viernes'].__str__()
                Sabado = form['Sabado'].__str__()
                Domingo = form['Domingo'].__str__()
                anotaciones = form['anotaciones'].__str__()  
                
                
                context ={
                    'cantidad_max_periodos': cantidad_max_periodo,
                    'Lunes': Lunes, 'Martes': Martes, 'Miercoles': Miercoles, 'Jueves': Jueves, 'Viernes': Viernes, 'Sabado': Sabado, 'Domingo': Domingo,
                    'anotaciones': anotaciones,
                }
                return JsonResponse(context, safe=False, status=200)

            profesores = list(Profesor.objects.filter(
                status_model=True).values())
            profesores_list = []
            for p in profesores:
                try:
                    profesor = EstadoProfesorHorario.objects.get(
                        horario = Horario.objects.get(id=id_horario),
                        profesor = Profesor.objects.get(id=p['id'])
                    )
                except EstadoProfesorHorario.DoesNotExist:
                    
                    profesor = EstadoProfesorHorario.objects.create(
                        horario = Horario.objects.get(id=id_horario),
                        profesor = Profesor.objects.get(id=p['id']),
                        cantidad_max_periodo = Horario.objects.get(id=id_horario).Cantidad_periodos(),

                    )
                finally:
                    profesores_list.append({
                        'id': profesor.id,
                        'nombre': p['nombre'],
                        'alias': p['alias'],
                        'activo': profesor.activo,
                        'id_profesor': p['id']
                    })
            return JsonResponse(profesores_list, safe=False)
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
