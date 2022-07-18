from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('aula/', aula, name='aula'),
    path('grado/', grado, name='grado'),
    path('profesor/', profesor, name='profesor'),
]

