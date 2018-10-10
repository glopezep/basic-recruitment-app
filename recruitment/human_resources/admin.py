from django.contrib import admin

from .models import *

from candidates.models import Candidato, Experiencia

# Register your models here.


@admin.register(Competencia)
class CompetenciaAdmin(admin.ModelAdmin):
    list_display = (
        'description',
        'estado'
    )


@admin.register(Idioma)
class IdiomaAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'estado'
    )


@admin.register(Capacitacion)
class CapacitacionAdmin(admin.ModelAdmin):
    list_display = (
        'descripcion',
        'nivel',
        'fecha_desde',
        'fecha_hasta',
        'institucion',
        'estado'
    )


@admin.register(Puesto)
class PuestoAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'nivel_riesgo',
        'nivel_minimo_salario',
        'nivel_maximo_salario',
        'estado',
    )


@admin.register(Experiencia)
class ExperienciaAdmin(admin.ModelAdmin):
    list_display = (
        'empresa',
        'puesto_ocupado',
        'fecha_desde',
        'fecha_hasta',
        'salario'
    )


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'cedula',
        'nombre',
        'fecha_ingreso',
        'departamento',
        'salario_mensual',
        'estado'
    )

@admin.register(Candidato)
class CandidatoAdmin(admin.ModelAdmin):
    list_display = (
        'cedula',
        'nombre',
        'departamento',
        'puesto',
        'recomendado_por'
    )
