from django.db import models
from django.utils import timezone
from django.forms import model_to_dict
from django.contrib.auth.models import User


# User 
class Pregunta(models.Model):
    activo = models.BooleanField(default=True)
    pregunta = models.CharField(max_length=100, unique=True)
    respuesta = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_modificacion = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.pregunta

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        db_table = 'pregunta'
        verbose_name = 'pregunta'
        verbose_name_plural = 'preguntas'

class Grado(models.Model):
    activo = models.BooleanField(default=True)
    nombre = models.CharField(
        max_length=50, unique=True, blank=False, null=False)
    alias = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    status_model = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    
   
    class Meta:
        verbose_name = 'Grado'
        verbose_name_plural = 'Grados'
        ordering = ['activo','nombre',]


class Profesor(models.Model):
    activo = models.BooleanField(default=True)
    nombre = models.CharField(
        max_length=50, unique=True, blank=False, null=False)
    alias = models.CharField(max_length=50, blank=True, null=True)
    status_model = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'
        ordering = ['activo','nombre',]


class Materia(models.Model):
    activo = models.BooleanField(default=True)
    nombre = models.CharField(
        max_length=50, unique=True, blank=False, null=False)
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE)
    status_model = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Materia'
        verbose_name_plural = 'Materias'
        ordering = ['activo','nombre',]

class Aula(models.Model):
    activo = models.BooleanField(default=True)
    nombre = models.CharField(
        max_length=50, unique=True, blank=False, null=False)
    state = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Aula'
        verbose_name_plural = 'Aulas'
        ordering = ['activo','nombre',]


class Horario(models.Model):
    activo = models.BooleanField(default=True)
    nombre = models.CharField(
        max_length=50, unique=True, blank=False, null=False)
    descripcion = models.TextField(blank=True, null=True)
    estado_del_horario = models.CharField(
        max_length=50, blank=True, null=True)
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Plantilla de horario'
        verbose_name_plural = 'Plantillas de horario'
        ordering = ['activo','nombre',]

class EstadoProfesorHorario(models.Model):
    activo = models.BooleanField(default=True)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Estado de profesor en horario'
        verbose_name_plural = 'Estados de profesor en horario'
        ordering = ['activo',]


class EstadoGradoHorario(models.Model):
    activo = models.BooleanField(default=True)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    grado = models.ForeignKey(Grado, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.activo)

    class Meta:
        verbose_name = 'Estado de grado en horario'
        verbose_name_plural = 'Estados de grado en horario'
        ordering = ['activo',]

# Estado_materias_horario


class EstadoMateriaHorario(models.Model):
    activo = models.BooleanField(default=True)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.activo)

    class Meta:
        verbose_name = 'Estado de materia en horario'
        verbose_name_plural = 'Estados de materia en horario'
        ordering = ['activo',]
class EstadoAulaHorario(models.Model):
    activo = models.BooleanField(default=True)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    aula = models.ForeignKey(Aula, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.activo)

    class Meta:
        verbose_name = 'Estado de aula en horario'
        verbose_name_plural = 'Estados de aula en horario'
        ordering = ['activo',]

class Asignatura(models.Model):
    activo = models.BooleanField(default=True)
    profesor = models.ForeignKey(Profesor, on_delete=models.PROTECT)
    materia = models.ForeignKey(Materia, on_delete=models.PROTECT)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Asignatura'
        verbose_name_plural = 'Asignaturas'
        ordering = ['activo',]

# Periodo


class Periodo(models.Model):
    activo = models.BooleanField(default=True)
    nombre = models.CharField(max_length= 50)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    dia = models.CharField(max_length=10, blank=False, null=False)
    hora_inicio = models.TimeField(blank=False, null=False)
    hora_fin = models.TimeField(blank=False, null=False)
    
    def __str__(self):
        return self.dia + ' ' + self.hora_inicio.strftime('%H:%M') + '-' + self.hora_fin.strftime('%H:%M')

    class Meta:
        verbose_name = 'Periodo'
        verbose_name_plural = 'Periodos'
        ordering = ['dia', 'hora_inicio']
