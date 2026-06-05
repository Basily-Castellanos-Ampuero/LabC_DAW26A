from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import DestinosTuristicos
from .forms import DestinoForm


def lista_destinos(request):
    destinos = DestinosTuristicos.objects.all()
    return render(request, 'destinos_turisticos/lista.html', {'destinos': destinos})


def agregar_destino(request):
    if request.method == 'POST':
        form = DestinoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Destino turístico agregado correctamente.')
            return redirect('lista_destinos')
    else:
        form = DestinoForm()
    return render(request, 'destinos_turisticos/form.html', {'form': form, 'accion': 'Agregar'})


def modificar_destino(request, pk):
    destino = get_object_or_404(DestinosTuristicos, pk=pk)
    if request.method == 'POST':
        form = DestinoForm(request.POST, request.FILES, instance=destino)
        if form.is_valid():
            form.save()
            messages.success(request, 'Destino turístico modificado correctamente.')
            return redirect('lista_destinos')
    else:
        form = DestinoForm(instance=destino)
    return render(request, 'destinos_turisticos/form.html', {'form': form, 'accion': 'Modificar'})


def eliminar_destino(request, pk):
    destino = get_object_or_404(DestinosTuristicos, pk=pk)
    if request.method == 'POST':
        destino.delete()
        messages.success(request, 'Destino turístico eliminado correctamente.')
        return redirect('lista_destinos')
    return render(request, 'destinos_turisticos/confirmar_eliminar.html', {'destino': destino})
