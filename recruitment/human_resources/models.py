from django.db import models

from django.contrib.auth.models import User

from .validators import validar_cedula

# Create your models here.
class Competencia(models.Model):
  description = models.CharField(max_length=100)
  estado = models.BooleanField(default=True)

  def __str__(self):
    return self.description


class Idioma(models.Model):
  nombre = models.CharField(max_length=100)
  estado = models.BooleanField(default=True)

  def __str__(self):
    return self.nombre


class Capacitacion(models.Model):
  NIVELES = (
    ('Grado', 'Grado'),
    ('Post Grado', 'Post Grado'),
    ('Maestría', 'Maestría'),
    ('Doctorado', 'Doctorado'),
    ('Técnico', 'Técnico'),
    ('Gestión', 'Gestión'),
  )

  descripcion = models.CharField(max_length=100)
  nivel = models.CharField(max_length=100, choices=NIVELES)
  fecha_desde = models.DateField()
  fecha_hasta = models.DateField()
  institucion = models.CharField(max_length=100)
  estado = models.BooleanField(default=True)

  def __str__(self):
    return self.descripcion


class Puesto(models.Model):
  NIVELES = (
    ('Alto', 'Alto'),
    ('Medio', 'Medio'),
    ('Bajo', 'Bajo'),
  )

  nombre = models.CharField(max_length=100)
  nivel_riesgo = models.CharField(max_length=100, choices=NIVELES)
  nivel_minimo_salario = models.IntegerField()
  nivel_maximo_salario = models.IntegerField()
  estado = models.BooleanField(default=True)

  def __str__(self):
    return self.nombre


class Empleado(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
  cedula = models.CharField(max_length=11, validators=[validar_cedula])
  nombre = models.CharField(max_length=100)
  fecha_ingreso = models.DateField()
  departamento = models.CharField(max_length=100)
  puesto = models.ForeignKey('Puesto',  on_delete=models.CASCADE)
  salario_mensual = models.IntegerField()
  estado = models.BooleanField(default=True)

  def __str__(self):
    return self.nombre

