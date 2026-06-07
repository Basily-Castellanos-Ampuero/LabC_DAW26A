from django.contrib import admin
from .models import Autor, Libro, Genero

admin.site.register(Autor)
admin.site.register(Genero)

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'año']
    filter_horizontal = ['generos']
