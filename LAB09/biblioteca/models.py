from django.db import models

# Relación Uno a Muchos: un Autor tiene muchos Libros
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    pais = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Autores"


# Relación Muchos a Muchos: un Libro tiene muchos Generos y viceversa
class Genero(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Géneros"


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    # Uno a muchos: cada libro pertenece a UN autor
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros')
    # Muchos a muchos: un libro puede tener varios géneros
    generos = models.ManyToManyField(Genero, blank=True)
    año = models.IntegerField()
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.titulo
