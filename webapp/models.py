from django.db import models
from django.utils import timezone
class Grado(models.Model):
    nombre = models.CharField(
        max_length=50, unique=True, blank=False, null=False)
    alias = models.CharField(max_length=50, blank=True, null=True)
    state = models.BooleanField(default=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('nombre',)
    def __str__(self):
        return self.nombre

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Grado'
        verbose_name_plural = 'Grados'
        ordering = ['nombre']


class Profesor(models.Model):
    nombre = models.CharField(
        max_length=50, unique=True, blank=False, null=False)
    alias = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'
        ordering = ['nombre']


class Materia(models.Model):
    nombre = models.CharField(
        max_length=50, unique=True, blank=False, null=False)
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Materia'
        verbose_name_plural = 'Materias'
        ordering = ['nombre']

class Aula(models.Model):
    nombre = models.CharField(
        max_length=50, unique=True, blank=False, null=False)
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Aula'
        verbose_name_plural = 'Aulas'
        ordering = ['nombre']


class Horario(models.Model):
    nombre = models.CharField(
        max_length=50, unique=True, blank=False, null=False)
    estado = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Plantilla de horario'
        verbose_name_plural = 'Plantillas de horario'
        ordering = ['nombre']

class EstadoProfesorHorario(models.Model):
    estado = models.BooleanField(default=True)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete=models.PROTECT)

    
    class Meta:
        verbose_name = 'Estado de profesor en horario'
        verbose_name_plural = 'Estados de profesor en horario'
        ordering = ['estado']


class EstadoGradoHorario(models.Model):
    estado = models.BooleanField(default=True)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    grado = models.ForeignKey(Grado, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.estado)

    class Meta:
        verbose_name = 'Estado de grado en horario'
        verbose_name_plural = 'Estados de grado en horario'
        ordering = ['estado']

# Estado_materias_horario


class EstadoMateriaHorario(models.Model):
    estado = models.BooleanField(default=True)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.estado)

    class Meta:
        verbose_name = 'Estado de materia en horario'
        verbose_name_plural = 'Estados de materia en horario'
        ordering = ['estado']
class EstadoAulaHorario(models.Model):
    estado = models.BooleanField(default=True)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    aula = models.ForeignKey(Aula, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.estado)

    class Meta:
        verbose_name = 'Estado de aula en horario'
        verbose_name_plural = 'Estados de aula en horario'
        ordering = ['estado']

class Asignatura(models.Model):
    estado = models.BooleanField(default=True)
    profesor = models.ForeignKey(Profesor, on_delete=models.PROTECT)
    materia = models.ForeignKey(Materia, on_delete=models.PROTECT)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Asignatura'
        verbose_name_plural = 'Asignaturas'
        ordering = ['estado']

# Periodo


class Periodo(models.Model):
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
