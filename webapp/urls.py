from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('profesores/', ProfesoresView.as_view(), name='profesores'),
    path('grados/', GradosView.as_view(), name='grados'),
    path('usuario/', UsuarioView.as_view(), name='usuario'),
    path('exportar/', ExportarView.as_view(), name='exportar'),
]
