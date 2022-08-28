from django.shortcuts import render
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView


#home con validacion de usuario con login_required
class HomeView(TemplateView):
    template_name = 'web/home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return super().get_context_data(**kwargs)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return redirect('login')
        

#login con validacion de usuario con login_required


