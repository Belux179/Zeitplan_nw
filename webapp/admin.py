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