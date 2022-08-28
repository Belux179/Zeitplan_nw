from django.contrib import admin
from .models import *

# Register your models here.
"""
class AulaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'capacidad', 'grado', 'profesor')
    list_filter = ('grado', 'profesor')
    search_fields = ('nombre',)
    ordering = ('nombre',)
    fields = ('nombre', 'capacidad', 'grado', 'profesor')
    list_editable = ['capacidad'] 
    list_per_page = 5
admin.site.register(Aula, AulaAdmin)
"""

class GradoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'alias')
    search_fields = ('nombre','alias')
    ordering = ('nombre',)
    list_per_page = 5

class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'alias')
    search_fields = ('nombre','alias')
    ordering = ('nombre',)
    list_per_page = 5

class MateriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'grado',)
    list_filter = ('grado',)
    search_fields = ('nombre',)
    ordering = ('nombre',)
    fields = ('nombre', 'grado')
    list_per_page = 5

class AulaAdmin(admin.ModelAdmin):
    list_display = ('nombre', )
    search_fields = ('nombre',)
    ordering = ('nombre',)
    fields = ('nombre', 'capacidad', 'grado', 'profesor')
    list_per_page = 5


class HorarioAdmin(admin.ModelAdmin):
    list_display = ('nombre','estado', 'description')
    list_filter = ('estado',)
    search_fields = ('nombre',)
    #para que sea editable
    list_editable = ['estado']
    ordering = ('nombre',)
    fields = ('nombre', 'estado', 'description')
    list_per_page = 5

class EstadoProfesorHorarioAdmin(admin.ModelAdmin):
    list_display = ('estado', 'horario', 'profesor')
    list_filter = ('estado', 'horario', 'profesor')
    search_fields = ('estado', 'horario', 'profesor')
    ordering = ('estado', 'horario', 'profesor')
    fields = ('estado', 'horario', 'profesor')
    list_per_page = 5


class EstadoGradoHorarioAdmin(admin.ModelAdmin):
    list_display = ('estado', 'horario', 'grado')
    list_filter = ('estado', 'horario', 'grado')
    search_fields = ('estado', 'horario', 'grado')
    ordering = ('estado', 'horario', 'grado')
    fields = ('estado', 'horario', 'grado')
    list_per_page = 5

class EstadoMateriaHorarioAdmin(admin.ModelAdmin):
    list_display = ('estado', 'horario', 'materia')
    list_filter = ('estado', 'horario', 'materia')
    search_fields = ('estado', 'horario', 'materia')
    ordering = ('estado', 'horario', 'materia')
    fields = ('estado', 'horario', 'materia')
    list_per_page = 5


class EstadoAulaHorarioAdmin(admin.ModelAdmin):
    list_display = ('estado', 'horario', 'aula')
    list_filter = ('estado', 'horario', 'aula')
    search_fields = ('estado', 'horario', 'aula')
    ordering = ('estado', 'horario', 'aula')
    fields = ('estado', 'horario', 'aula')
    list_per_page = 5



class AsignaturaAdmin(admin.ModelAdmin):
    list_display = ('estado', 'profesor', 'materia', 'horario')
    list_filter = ('estado', 'profesor', 'materia', 'horario')
    search_fields = ('estado', 'profesor', 'materia', 'horario')
    ordering = ('estado', 'profesor', 'materia', 'horario')
    fields = ('estado', 'profesor', 'materia', 'horario')
    list_per_page = 5


class PeriodoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'asignatura', 'dia', 'hora_inicio', 'hora_fin')
    list_filter = ('asignatura', 'dia', 'hora_inicio', 'hora_fin')
    search_fields = ('nombre', 'asignatura', 'dia', 'hora_inicio', 'hora_fin')
    ordering = ('nombre', 'asignatura', 'dia', 'hora_inicio', 'hora_fin')
    fields = ('nombre', 'asignatura', 'dia', 'hora_inicio', 'hora_fin')
    list_per_page = 5

    
admin.site.register(Grado, GradoAdmin)
admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Materia, MateriaAdmin)
admin.site.register(Horario, HorarioAdmin)
admin.site.register(EstadoProfesorHorario, EstadoProfesorHorarioAdmin)
admin.site.register(EstadoGradoHorario, EstadoGradoHorarioAdmin)
admin.site.register(EstadoMateriaHorario, EstadoMateriaHorarioAdmin)
admin.site.register(Asignatura, AsignaturaAdmin)
admin.site.register(Periodo, PeriodoAdmin)



