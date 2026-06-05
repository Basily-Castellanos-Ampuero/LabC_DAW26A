from django.db import models


class DestinosTuristicos(models.Model):
    nombreCiudad = models.CharField(max_length=100)
    descripcionCiudad = models.TextField()
    imagenCiudad = models.ImageField(upload_to='destinos/', blank=True, null=True)
    precioTour = models.DecimalField(max_digits=8, decimal_places=2)
    ofertaTour = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Destino Turístico'
        verbose_name_plural = 'Destinos Turísticos'

    def __str__(self):
        return self.nombreCiudad
