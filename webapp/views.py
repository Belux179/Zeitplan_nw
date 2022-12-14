from multiprocessing import context
from re import U
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

# user
from django.contrib.auth.models import User
from django import forms


# home con validacion de usuario con login_required
class HomeView(TemplateView):
    template_name = 'web/home.html'
    model = Horario

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(HomeView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['horarios'] = Horario.objects.all()
        return context


class ProfesoresView(ListView):
    model = Profesor
    template_name = 'web/profesor.html'
    form_class = ProfesorForm

    # usando get_context_data y dispatch para enviar el formulario y validar el usuario
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
    form_class = GradoForm
    second_form_class = MateriaForm

    # usando get_context_data y dispatch para enviar el formulario y validar el usuario
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'form_grado' not in context:
            context['form_grado'] = GradoForm
        if 'form_materia' not in context:
            context['form_materia'] = MateriaForm
        context['Grados'] = Grado.objects.all()
        context['Materias'] = Materia.objects.all()
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.POST.get('tipo') == 'grado':
            form = self.form_class(request.POST)
            form_grado, form_materia = form, self.second_form_class()
        if request.POST.get('tipo') == 'materia':
            form = self.second_form_class(request.POST)
            form_grado, form_materia = self.form_class(), form
        if form.is_valid():
            form.save()
            return redirect('grados')
        return render(request, self.template_name, {'form_grado': form_grado, 'form_materia': form_materia, 'Grados': Grado.objects.all(), 'Materias': Materia.objects.all()})


class UsuarioView(ListView):
    template_name = 'web/usuario.html'
    model = User
    form_class = UserForm
    second_form_class = PreguntasForm

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(UsuarioView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # actualizar el usuario que se esta logueando
        context['form'] = self.form_class(instance=self.request.user)
        # form de preguntas de recuperacion del usuario que se esta logueando
        # preguntas que el usuario sea el usuario que se esta logueando
        
        context['form_pregunta'] = self.second_form_class(instance=self.request.user)
        
        return context
        
    def post(self, request, *args, **kwargs):
        if request.POST.get('tipo') == 'usuario':
            form = self.form_class(request.POST, instance=self.request.user)
            form_usuario, form_pregunta = form, self.second_form_class(
                instance=self.request.user)
        if request.POST.get('tipo') == 'pregunta':
            form = self.second_form_class(request.POST, instance=self.request.user)
            form_usuario, form_pregunta = form, self.second_form_class(
                request.POST, instance=self.request.user)
        if form.is_valid():
            form.save()
            return redirect('usuario')
        return render(request, self.template_name, {'form': form_usuario, 'form_pregunta': form_pregunta})


class ExportarView(ListView):
    template_name = 'web/exportar.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)  # """
