from django import forms
from .models import Alumno, Curso, NotaAlumnoPorCurso


class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['codigo', 'nombre', 'apellido', 'email']


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['codigo', 'nombre', 'creditos']


class NotaForm(forms.ModelForm):
    class Meta:
        model = NotaAlumnoPorCurso
        fields = ['alumno', 'curso', 'nota']
