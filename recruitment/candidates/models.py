from django.db import models

from django.contrib.auth.models import User

from .validators import validar_cedula

from human_resources.models import (
  Puesto,
  Competencia,
  Capacitacion,
  Empleado,
)


class Experiencia(models.Model):
  empresa = models.CharField(max_length=100)
  puesto_ocupado = models.ForeignKey(Puesto, on_delete=models.CASCADE)
  fecha_desde = models.DateField()
  fecha_hasta = models.DateField()
  salario = models.IntegerField()

  def __str__(self):
    return self.puesto_ocupado.nombre


class Candidato(models.Model):
  cedula = models.CharField(max_length=11, validators=[validar_cedula])
  nombre = models.CharField(max_length=100)
  puesto = models.ForeignKey(Puesto, on_delete=models.CASCADE)
  departamento = models.CharField(max_length=100)
  salario_aspira = models.IntegerField(blank=True)
  competencias = models.ManyToManyField(Competencia, blank=True)
  capacitaciones = models.ManyToManyField(Capacitacion, blank=True)
  experiencias = models.ManyToManyField(Experiencia, blank=True)
  recomendado_por = models.ForeignKey(Empleado,  on_delete=models.CASCADE, null=True, blank=True)
  esta_reclutado = models.BooleanField(null=True, blank=True, default=False)

  def __str__(self):
    return self.nombre
