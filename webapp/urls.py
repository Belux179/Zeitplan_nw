from django.urls import path
from .views import *
from .ajax import *

urlpatterns = []

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
    path('newhorario/ajax/', NewHorarioAjax.as_view(), name='newhorario_ajax'),
]
#"""
urlpatterns += [
    #path('plantilla/<int:id_horario>/', PlantillaView.as_view(), name='plantilla'),
    #path('select_profesor/<int:id_horario>/', SelectProfesorView.as_view(), name='select_profesor'),
    #path('select_grado/<int:id_horario>/', SelectGradoView.as_view(), name='select_grado'),
    #path('select_asignatura/<int:id_horario>/', AsignaturasView.as_view(), name='asignaturas'),
    #path('select_periodo/<int:id_horario>/', SelectPeriodoView.as_view(), name='select_periodo'),
    #path('horario/<int:id_horario>/', HorarioView.as_view(), name='horario'),
    
    #path('horario/<int:id_horario>/pdf/', HorarioPDFView.as_view(), name='horario_pdf')
]
