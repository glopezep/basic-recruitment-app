from django import forms

from .models import Candidato, Experiencia


class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidato
        fields = (
            'cedula',
            'nombre',
            'puesto',
            'departamento',
            'salario_aspira',
            'competencias',
            'capacitaciones',
            'experiencias',
            'recomendado_por',
        )


class ExperienciaForm(forms.ModelForm):
    class Meta:
        model = Experiencia
        fields = (
            'empresa',
            'puesto_ocupado',
            'fecha_desde',
            'fecha_hasta',
            'salario',
        )
