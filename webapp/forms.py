from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
# user
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class PreguntasForm(forms.ModelForm):
    pregunta = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Pregunta'}))
    respuesta = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Respuesta'}))
    usuario = forms.Select(
        attrs={'class': 'form-control', 'placeholder': 'Usuario'})

    class Meta:
        model = Pregunta
        fields = ['pregunta', 'respuesta', 'usuario']


class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario', max_length=100)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)


class GradoForm(forms.ModelForm):

    class Meta:
        model = Grado
        fields = ['nombre', 'alias']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del grado', 'id': 'nombre_grado_form_grado'}),
            'alias': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Alias del grado', 'id': 'alias_grado_form_grado'}),

        }
        labels = {
            'nombre': 'Nombre del grado',
            'alias': 'Alias del grado',
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
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre', 'id': 'nombre_profesor_form_profesor'}),
            'alias': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Alias', 'id': 'alias_profesor_form_profesor'}),
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


"""class ProfesorFormUpdate(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['id','nombre', 'alias']
        widgets = {
            'id': forms.HiddenInput(attrs={'class': 'form-control', 'placeholder': 'Id', 'id': 'id_profesor_form_profesor'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre', 'id': 'nombre_profesor_form_update_profesor'}),
            'alias': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Alias', 'id': 'alias_profesor_form_update_profesor'}),
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
"""


class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ['nombre', 'grado']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre', 'id': 'nombre_materia_form_materia'}),
            'grado': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Grado', 'id': 'grado_materia_form_materia'}),
        }
        labels = {
            'nombre': 'Nombre',
            'grado': 'Grado',
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
        fields = ['nombre', 'estado_del_horario', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'estado_del_horario': forms.TextInput(attrs={'class': 'form-control', 'type': 'hidden'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripción',
        }
        help_texts = {
            'nombre': 'Ingrese el nombre del horario',
            'descripcion': 'Ingrese la descripción del horario',
        }
        error_messages = {
            'nombre': {
                'max_length': 'Nombre demasiado largo',
                'required': 'Nombre requerido',
            },
            'descripcion': {
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
            'profesor': 'Profesor',
            'materia': 'Materia',
            'horario': 'Horario',
        }
        help_texts = {
            'profesor': 'Seleccione el profesor de la asignatura',
            'materia': 'Seleccione la materia de la asignatura',
            'horario': 'Seleccione el horario de la asignatura',
        }
        error_messages = {
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
# """
