from django.http import JsonResponse
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *


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
            #filtrar por  'status_model' = True
            profesores = list(Profesor.objects.filter(status_model=True).values())
            return JsonResponse(profesores, safe=False)
        except Exception as e:
            print(e)
            return JsonResponse({'message': str(e)}, status=400)


# grado
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

# materia


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
                    #agregar el valor inicial de grado de acuerdo con el id del request id_grado
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
                materia['grado'] = Grado.objects.get(id=materia['grado_id']).nombre
            return JsonResponse(materias, safe=False)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=400)



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
