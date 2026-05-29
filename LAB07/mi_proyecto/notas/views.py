from django.shortcuts import render, redirect
from .models import Alumno, Curso, NotaAlumnoPorCurso
from .forms import AlumnoForm, CursoForm, NotaForm


def inicio(request):
    return render(request, 'notas/inicio.html')


def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'notas/lista_alumnos.html', {'alumnos': alumnos})


def crear_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_alumnos')
    else:
        form = AlumnoForm()
    return render(request, 'notas/form_alumno.html', {'form': form, 'titulo': 'Nuevo Alumno'})


def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'notas/lista_cursos.html', {'cursos': cursos})


def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_cursos')
    else:
        form = CursoForm()
    return render(request, 'notas/form_curso.html', {'form': form, 'titulo': 'Nuevo Curso'})


def lista_notas(request):
    notas = NotaAlumnoPorCurso.objects.select_related('alumno', 'curso').all()
    return render(request, 'notas/lista_notas.html', {'notas': notas})


def crear_nota(request):
    if request.method == 'POST':
        form = NotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_notas')
    else:
        form = NotaForm()
    return render(request, 'notas/form_nota.html', {'form': form, 'titulo': 'Registrar Nota'})
