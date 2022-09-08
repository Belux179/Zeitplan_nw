from django.shortcuts import render
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.http import JsonResponse


#home con validacion de usuario con login_required
class HomeView(TemplateView):
    template_name = 'web/home.html'
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ProfesoresView(ListView):
    model = Profesor
    template_name = 'web/profesor.html'
    form_class = ProfesorForm
    
    #usando get_context_data y dispatch para enviar el formulario y validar el usuario
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        context['Profesores'] = Profesor.objects.all()
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profesores')
        return render(request, self.template_name, {'form': form, 'Profesores': Profesor.objects.all()})

class GradosView(ListView):
    model = Grado
    template_name = 'web/grado.html'
    context_object_name = 'grados'
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'grados': Grado.objects.all()})


class UsuarioView(ListView):
    template_name = 'web/usuario.html'
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ExportarView(ListView):
    template_name = 'web/exportar.html'
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)