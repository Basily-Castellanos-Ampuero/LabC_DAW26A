from django.contrib import admin
from .models import Alumno, Curso, NotaAlumnoPorCurso

admin.site.register(Alumno)
admin.site.register(Curso)
admin.site.register(NotaAlumnoPorCurso)
