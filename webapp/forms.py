from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario', max_length=100)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
  
class GradoForm(forms.ModelForm):
    class Meta:
        model = Grado
        fields = ['nombre', 'alias']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del grado'}),
            'alias': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Alias del grado'}),
        }
        labels = {
            'nombre': 'Nombre del grado',
            'alias': 'Alias del grado',
        }
        help_texts = {
            'nombre': 'Ingrese el nombre del grado',
            'alias': 'Ingrese el alias del grado',
        }
        error_messages = {
            'nombre': {
                'required': 'El nombre del grado es obligatorio',
                'max_length': 'El nombre del grado no puede tener mas de 50 caracteres',
                'min_length': 'El nombre del grado no puede tener menos de 3 caracteres',
            },
            'alias': {
                'max_length': 'El alias del grado no puede tener mas de 50 caracteres',
                'min_length': 'El alias del grado no puede tener menos de 3 caracteres',
            },
        }


class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'alias']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'alias': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Alias'}),
        }
        labels = {
            'nombre': 'Nombre',
            'alias': 'Alias',
        }
        error_messages = {
            'nombre': {
                'max_length': "Nombre muy largo",
                'required': "Nombre requerido",
            },
            'alias': {
                'max_length': "Alias muy largo",
            },
        }


class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ['nombre', 'grado']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'grado': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'nombre': 'Nombre',
            'grado': 'Grado',
        }
        help_texts = {
            'nombre': 'Nombre de la materia',
            'grado': 'Grado de la materia',
        }
        error_messages = {
            'nombre': {
                'max_length': "Nombre muy largo",
                'required': "Nombre requerido",
            },
            'grado': {
                'required': "Grado requerido",
            },
        }


class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = ['nombre', 'estado', 'description']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'nombre': 'Nombre',
            'estado': 'Estado',
            'description': 'Descripción',
        }
        help_texts = {
            'nombre': 'Ingrese el nombre del horario',
            'estado': 'Seleccione el estado del horario',
            'description': 'Ingrese la descripción del horario',
        }
        error_messages = {
            'nombre': {
                'max_length': 'Nombre demasiado largo',
                'required': 'Nombre requerido',
            },
            'estado': {
                'required': 'Estado requerido',
            },
            'description': {
                'max_length': 'Descripción demasiado larga',
                'required': 'Descripción requerida',
            },
        }


class AsignaturaForm(forms.ModelForm):
    class Meta:
        model = Asignatura
        fields = ['profesor', 'materia',  'horario']
        widgets = {
            'profesor': forms.Select(attrs={'class': 'form-control'}),
            'materia': forms.Select(attrs={'class': 'form-control'}),
            'horario': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'estado': 'Estado',
            'profesor': 'Profesor',
            'materia': 'Materia',
            'horario': 'Horario',
        }
        help_texts = {
            'estado': 'Seleccione el estado de la asignatura',
            'profesor': 'Seleccione el profesor de la asignatura',
            'materia': 'Seleccione la materia de la asignatura',
            'horario': 'Seleccione el horario de la asignatura',
        }
        error_messages = {
            'estado': {
                'required': 'Estado requerido',
            },
            'profesor': {
                'required': 'Profesor requerido',
            },
            'materia': {
                'required': 'Materia requerida',
            },
            'horario': {
                'required': 'Horario requerido',
            },
        }
