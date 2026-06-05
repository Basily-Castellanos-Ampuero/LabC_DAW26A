from django.contrib import admin
from .models import DestinosTuristicos


@admin.register(DestinosTuristicos)
class DestinosTuristicosAdmin(admin.ModelAdmin):
    list_display = ('nombreCiudad', 'precioTour', 'ofertaTour')
    list_filter = ('ofertaTour',)
    search_fields = ('nombreCiudad',)
