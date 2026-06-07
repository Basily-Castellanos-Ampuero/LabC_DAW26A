from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# PDF
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import io

from .models import Autor, Libro, Genero
from .forms import AutorForm, LibroForm, GeneroForm, EmailForm


# ── INICIO ──────────────────────────────────────────────────────────────────

def inicio(request):
    total_autores = Autor.objects.count()
    total_libros = Libro.objects.count()
    total_generos = Genero.objects.count()
    return render(request, 'biblioteca/inicio.html', {
        'total_autores': total_autores,
        'total_libros': total_libros,
        'total_generos': total_generos,
    })


# ── AUTORES (Uno a Muchos - lado "uno") ─────────────────────────────────────

def autor_lista(request):
    autores = Autor.objects.all()
    return render(request, 'biblioteca/autor_lista.html', {'autores': autores})


def autor_nuevo(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Autor creado correctamente.')
            return redirect('autor_lista')
    else:
        form = AutorForm()
    return render(request, 'biblioteca/formulario.html', {'form': form, 'titulo': 'Nuevo Autor'})


def autor_editar(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Autor actualizado.')
            return redirect('autor_lista')
    else:
        form = AutorForm(instance=autor)
    return render(request, 'biblioteca/formulario.html', {'form': form, 'titulo': 'Editar Autor'})


def autor_eliminar(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        autor.delete()
        messages.success(request, 'Autor eliminado.')
        return redirect('autor_lista')
    return render(request, 'biblioteca/confirmar_eliminar.html', {'objeto': autor, 'tipo': 'autor'})


def autor_detalle(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    libros = autor.libros.all()   # relación inversa Uno a Muchos
    return render(request, 'biblioteca/autor_detalle.html', {'autor': autor, 'libros': libros})


# ── GÉNEROS (Muchos a Muchos - lado auxiliar) ────────────────────────────────

def genero_lista(request):
    generos = Genero.objects.all()
    return render(request, 'biblioteca/genero_lista.html', {'generos': generos})


def genero_nuevo(request):
    if request.method == 'POST':
        form = GeneroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Género creado.')
            return redirect('genero_lista')
    else:
        form = GeneroForm()
    return render(request, 'biblioteca/formulario.html', {'form': form, 'titulo': 'Nuevo Género'})


def genero_eliminar(request, pk):
    genero = get_object_or_404(Genero, pk=pk)
    if request.method == 'POST':
        genero.delete()
        messages.success(request, 'Género eliminado.')
        return redirect('genero_lista')
    return render(request, 'biblioteca/confirmar_eliminar.html', {'objeto': genero, 'tipo': 'género'})


# ── LIBROS (Uno a Muchos - lado "muchos" / Muchos a Muchos con Géneros) ──────

def libro_lista(request):
    libros = Libro.objects.select_related('autor').prefetch_related('generos').all()
    return render(request, 'biblioteca/libro_lista.html', {'libros': libros})


def libro_nuevo(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Libro creado correctamente.')
            return redirect('libro_lista')
    else:
        form = LibroForm()
    return render(request, 'biblioteca/formulario.html', {'form': form, 'titulo': 'Nuevo Libro'})


def libro_editar(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            messages.success(request, 'Libro actualizado.')
            return redirect('libro_lista')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'biblioteca/formulario.html', {'form': form, 'titulo': 'Editar Libro'})


def libro_eliminar(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
        messages.success(request, 'Libro eliminado.')
        return redirect('libro_lista')
    return render(request, 'biblioteca/confirmar_eliminar.html', {'objeto': libro, 'tipo': 'libro'})


# ── PDF ──────────────────────────────────────────────────────────────────────

def generar_pdf(request):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4, title='Catálogo de Libros')
    estilos = getSampleStyleSheet()
    elementos = []

    # Título
    elementos.append(Paragraph('Catálogo de la Biblioteca', estilos['Title']))
    elementos.append(Spacer(1, 12))

    # Tabla de libros
    libros = Libro.objects.select_related('autor').prefetch_related('generos').all()

    datos = [['Título', 'Autor', 'Año', 'Géneros']]
    for libro in libros:
        generos_str = ', '.join(g.nombre for g in libro.generos.all()) or '-'
        datos.append([libro.titulo, libro.autor.nombre, str(libro.año), generos_str])

    tabla = Table(datos, colWidths=[200, 130, 50, 130])
    tabla.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey]),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('TOPPADDING', (0, 1), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 4),
    ]))
    elementos.append(tabla)

    doc.build(elementos)
    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf',
                        headers={'Content-Disposition': 'inline; filename="catalogo_libros.pdf"'})


# ── EMAIL ────────────────────────────────────────────────────────────────────

def enviar_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            destinatario = form.cleaned_data['destinatario']
            asunto = form.cleaned_data['asunto']
            mensaje = form.cleaned_data['mensaje']
            try:
                send_mail(
                    asunto,
                    mensaje,
                    settings.DEFAULT_FROM_EMAIL,
                    [destinatario],
                    fail_silently=False,
                )
                messages.success(request,
                    f'Correo enviado a {destinatario}. '
                    '(En modo desarrollo el correo se imprime en la consola del servidor.)')
                return redirect('enviar_email')
            except Exception as e:
                messages.error(request, f'Error al enviar: {e}')
    else:
        form = EmailForm()
    return render(request, 'biblioteca/email.html', {'form': form})
