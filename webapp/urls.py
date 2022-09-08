from django.urls import path
from .views import *
from .ajax import *


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('profesores/', ProfesoresView.as_view(), name='profesores'),
    path('grados/', GradosView.as_view(), name='grados'),
    path('usuario/', UsuarioView.as_view(), name='usuario'),
    path('exportar/', ExportarView.as_view(), name='exportar'),
]

# ajax
urlpatterns += [
    path('profesores/ajax/', ProfesoresAjax.as_view(), name='profesores_ajax'),
    path('grados/ajax/', GradosAjax.as_view(), name='grados_ajax'),
    path('materias/ajax/', MateriasAjax.as_view(), name='materias_ajax'),
    path('horarios/ajax/', HorariosAjax.as_view(), name='horarios_ajax'),
    path('asignaturas/ajax/', AsignaturasAjax.as_view(), name='asignaturas_ajax'),
    path('periodos/ajax/', PeriodosAjax.as_view(), name='periodos_ajax'),
]