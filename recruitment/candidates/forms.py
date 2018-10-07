from django import forms

from .models import Candidato


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
